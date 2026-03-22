#!/usr/bin/env python3
"""
Hybrid RU translation pipeline for agency agent markdown files.

Goals:
- translate all missing source *.md agent files into translations/ru/<same-path>
- preserve markdown/code/frontmatter structure
- avoid translating code fences and inline code/link targets
- keep technical identifiers stable
"""

from __future__ import annotations

import argparse
import re
import sys
import time
from pathlib import Path

try:
    from deep_translator import GoogleTranslator
except Exception as exc:  # pragma: no cover
    print(
        "ERROR: deep-translator is not installed. "
        "Run: python3 -m pip install --user deep-translator",
        file=sys.stderr,
    )
    raise


SRC_DIRS = [
    "academic",
    "design",
    "engineering",
    "game-development",
    "marketing",
    "paid-media",
    "product",
    "project-management",
    "sales",
    "spatial-computing",
    "specialized",
    "support",
    "testing",
]

INLINE_CODE_RE = re.compile(r"`[^`]+`")
LINK_RE = re.compile(r"\[[^\]]+\]\([^)]+\)")


class Translator:
    def __init__(self) -> None:
        self._engine = GoogleTranslator(source="en", target="ru", timeout=12)
        self._cache: dict[str, str] = {}
        self._retries = 2
        self._chunk_chars = 3200

    def translate(self, text: str) -> str:
        raw = text.strip()
        if not raw:
            return text
        if raw in self._cache:
            return self._cache[raw]
        translated = raw
        for attempt in range(self._retries + 1):
            try:
                candidate = self._engine.translate(raw)
                if candidate:
                    translated = candidate
                break
            except Exception:
                if attempt < self._retries:
                    time.sleep(0.25)
        self._cache[raw] = translated
        return translated

    def translate_many(self, texts: list[str]) -> list[str]:
        if not texts:
            return []

        result = [""] * len(texts)
        pending: list[tuple[int, str]] = []

        for i, txt in enumerate(texts):
            raw = txt.strip()
            if not raw:
                result[i] = txt
            elif raw in self._cache:
                result[i] = self._cache[raw]
            else:
                pending.append((i, raw))

        pos = 0
        while pos < len(pending):
            chunk: list[tuple[int, str]] = []
            used = 0
            while pos < len(pending):
                idx, raw = pending[pos]
                cost = len(raw) + 24
                if chunk and used + cost > self._chunk_chars:
                    break
                chunk.append((idx, raw))
                used += cost
                pos += 1

            labeled = "\n".join(f"__AG_{n}__ {raw}" for n, (_, raw) in enumerate(chunk))
            translated_block = self.translate(labeled)

            parsed: dict[int, str] = {}
            for line in translated_block.splitlines():
                match = re.match(r"__AG_(\d+)__\s?(.*)$", line)
                if not match:
                    continue
                parsed[int(match.group(1))] = match.group(2)

            if len(parsed) == len(chunk):
                for n, (_, raw) in enumerate(chunk):
                    translated = parsed.get(n, raw).strip() or raw
                    self._cache[raw] = translated
            else:
                # Fallback: if marker parsing failed, safely translate line by line.
                for _, raw in chunk:
                    self._cache[raw] = self.translate(raw)

        for i, txt in enumerate(texts):
            if result[i]:
                continue
            raw = txt.strip()
            result[i] = self._cache.get(raw, raw)
        return result


def split_frontmatter(content: str) -> tuple[str, str]:
    if not content.startswith("---\n"):
        return "", content
    end = content.find("\n---\n", 4)
    if end == -1:
        return "", content
    front = content[: end + 5]
    body = content[end + 5 :]
    return front, body


def translate_frontmatter(front: str, tr: Translator) -> str:
    if not front:
        return front
    out: list[str] = []
    for line in front.splitlines(keepends=False):
        if line in ("---", ""):
            out.append(line)
            continue
        if ":" not in line:
            out.append(line)
            continue
        key, value = line.split(":", 1)
        stripped_key = key.strip()
        val = value.lstrip()
        # Keep identifiers stable, only localize human-facing text fields.
        if stripped_key in {"description", "vibe"} and val:
            quote = ""
            end_quote = ""
            raw = val
            if (raw.startswith('"') and raw.endswith('"')) or (
                raw.startswith("'") and raw.endswith("'")
            ):
                quote = raw[0]
                end_quote = raw[-1]
                raw = raw[1:-1]
            translated = tr.translate(raw)
            val = f"{quote}{translated}{end_quote}"
        out.append(f"{key}:{' ' if value.startswith(' ') else ''}{val}")
    return "\n".join(out) + "\n"


def protect_tokens(line: str) -> tuple[str, dict[str, str]]:
    tokens: dict[str, str] = {}

    def repl_link(match: re.Match[str]) -> str:
        token = f"__LINK_{len(tokens)}__"
        tokens[token] = match.group(0)
        return token

    def repl_code(match: re.Match[str]) -> str:
        token = f"__CODE_{len(tokens)}__"
        tokens[token] = match.group(0)
        return token

    tmp = LINK_RE.sub(repl_link, line)
    tmp = INLINE_CODE_RE.sub(repl_code, tmp)
    return tmp, tokens


def restore_tokens(line: str, tokens: dict[str, str]) -> str:
    out = line
    for token, original in tokens.items():
        out = out.replace(token, original)
    return out


def should_translate_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    # Do not translate pure markdown separators / code-only lines.
    if stripped in {"---", "***", "___"}:
        return False
    if re.fullmatch(r"[`~#>*\-\d\.\s|:+\[\]\(\)_/=\\]+", stripped):
        return False
    return True


def translate_body(body: str, tr: Translator) -> str:
    lines = body.splitlines(keepends=False)
    out: list[str] = lines[:]
    in_fence = False
    translate_idx: list[int] = []
    payloads: list[str] = []
    prefixes: list[str] = []
    token_maps: list[dict[str, str]] = []

    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if not should_translate_line(line):
            continue

        protected, tokens = protect_tokens(line)
        leading = protected[: len(protected) - len(protected.lstrip())]
        payload = protected[len(leading) :]
        translate_idx.append(i)
        payloads.append(payload)
        prefixes.append(leading)
        token_maps.append(tokens)

    translated_payloads = tr.translate_many(payloads)
    for i, line_idx in enumerate(translate_idx):
        rebuilt = prefixes[i] + translated_payloads[i]
        out[line_idx] = restore_tokens(rebuilt, token_maps[i])

    return "\n".join(out) + ("\n" if body.endswith("\n") else "")


def all_source_files(repo_root: Path) -> list[Path]:
    files: list[Path] = []
    for d in SRC_DIRS:
        root = repo_root / d
        if root.exists():
            files.extend(sorted(root.rglob("*.md")))
    return files


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--max-files", type=int, default=0)
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    out_root = repo_root / "translations" / "ru"
    out_root.mkdir(parents=True, exist_ok=True)

    src_files = all_source_files(repo_root)
    tr = Translator()

    translated = 0
    skipped = 0
    errors = 0

    for src in src_files:
        rel = src.relative_to(repo_root)
        target = out_root / rel
        if target.exists() and not args.overwrite:
            skipped += 1
            continue
        if args.max_files and translated >= args.max_files:
            break
        try:
            content = src.read_text(encoding="utf-8")
            front, body = split_frontmatter(content)
            t_front = translate_frontmatter(front, tr)
            t_body = translate_body(body, tr)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(t_front + t_body, encoding="utf-8")
            translated += 1
            print(f"[ok] {rel}", flush=True)
        except Exception as exc:  # pragma: no cover
            errors += 1
            print(f"[err] {rel}: {exc}", file=sys.stderr)

    print(
        f"done: translated={translated} skipped={skipped} errors={errors} "
        f"total_sources={len(src_files)}"
    )
    return 0 if errors == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
