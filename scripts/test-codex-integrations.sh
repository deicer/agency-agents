#!/usr/bin/env bash
#
# Smoke-test Codex integrations:
#   - legacy codex skills
#   - official codex skills
#   - curated codex subagents
#   - combined codex-all install flow
#
# Usage: ./scripts/test-codex-integrations.sh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

fail() {
  printf 'FAIL: %s\n' "$*" >&2
  exit 1
}

assert_eq() {
  local expected="$1"
  local actual="$2"
  local message="$3"
  if [[ "$expected" != "$actual" ]]; then
    fail "$message (expected: $expected, actual: $actual)"
  fi
}

assert_file_contains() {
  local file="$1"
  local needle="$2"
  if ! grep -Fq "$needle" "$file"; then
    fail "$file does not contain: $needle"
  fi
}

count_dirs() {
  local path="$1"
  find "$path" -mindepth 1 -maxdepth 1 -type d | wc -l | tr -d ' '
}

count_files() {
  local path="$1"
  find "$path" -mindepth 1 -maxdepth 1 -type f | wc -l | tr -d ' '
}

tmpdir="$(mktemp -d)"
trap 'rm -rf "$tmpdir"' EXIT

cd "$REPO_ROOT"

bash -n scripts/convert.sh scripts/install.sh scripts/codex_subagents.sh

rm -rf integrations/codex/skills integrations/codex-skills/skills integrations/codex-subagents/agents

./scripts/convert.sh --tool codex
./scripts/convert.sh --tool codex-skills
./scripts/convert.sh --tool codex-subagents

legacy_count="$(count_dirs integrations/codex/skills)"
official_count="$(count_dirs integrations/codex-skills/skills)"
subagent_count="$(count_files integrations/codex-subagents/agents)"

assert_eq "156" "$legacy_count" "legacy codex skill count mismatch"
assert_eq "156" "$official_count" "official codex skill count mismatch"
assert_eq "15" "$subagent_count" "codex subagent count mismatch"

assert_file_contains "integrations/codex-subagents/agents/agency-code-reviewer.toml" 'name = "agency-code-reviewer"'
assert_file_contains "integrations/codex-subagents/agents/agency-code-reviewer.toml" 'sandbox_mode = "read-only"'
assert_file_contains "integrations/codex-subagents/agents/agency-frontend-developer.toml" 'sandbox_mode = "workspace-write"'
assert_file_contains "integrations/codex-subagents/agents/agency-security-engineer.toml" 'model_reasoning_effort = "high"'

HOME="$tmpdir/home" CODEX_HOME="$tmpdir/codex" ./scripts/install.sh --tool codex --no-interactive
HOME="$tmpdir/home" CODEX_HOME="$tmpdir/codex" ./scripts/install.sh --tool codex-skills --no-interactive
HOME="$tmpdir/home" CODEX_HOME="$tmpdir/codex" ./scripts/install.sh --tool codex-subagents --no-interactive
HOME="$tmpdir/home" CODEX_HOME="$tmpdir/codex" ./scripts/install.sh --tool codex-all --no-interactive

assert_eq "156" "$(count_dirs "$tmpdir/codex/skills")" "legacy install count mismatch"
assert_eq "156" "$(count_dirs "$tmpdir/home/.agents/skills")" "official skill install count mismatch"
assert_eq "15" "$(count_files "$tmpdir/codex/agents")" "subagent install count mismatch"

assert_file_contains "$tmpdir/home/.agents/skills/agency-frontend-developer/SKILL.md" 'name: agency-frontend-developer'
assert_file_contains "$tmpdir/codex/agents/agency-reality-checker.toml" 'name = "agency-reality-checker"'
assert_file_contains "$tmpdir/codex/agents/agency-reality-checker.toml" '[[skills.config]]'
assert_file_contains "$tmpdir/codex/agents/agency-reality-checker.toml" 'enabled = true'

HOME="$tmpdir/autohome" CODEX_HOME="$tmpdir/autocodex" mkdir -p "$tmpdir/autocodex"
PATH="/usr/bin:/bin" HOME="$tmpdir/autohome" CODEX_HOME="$tmpdir/autocodex" ./scripts/install.sh --no-interactive

assert_eq "156" "$(count_dirs "$tmpdir/autohome/.agents/skills")" "autodetect official skill install count mismatch"
assert_eq "15" "$(count_files "$tmpdir/autocodex/agents")" "autodetect subagent install count mismatch"
if [[ -d "$tmpdir/autocodex/skills" ]]; then
  if [[ "$(count_dirs "$tmpdir/autocodex/skills")" != "0" ]]; then
    fail "autodetect should not install legacy codex skills"
  fi
fi

printf 'Codex integration smoke tests passed.\n'
