# 🔌 Интеграции

В этой папке собраны форматы и конвертированные артефакты для разных agentic coding tools.

[English version](./README.md)

## Поддерживаемые инструменты

- **Claude Code** — нативные `.md` agents, можно использовать почти без конвертации
- **GitHub Copilot** — нативные `.md` agents
- **Antigravity** — `SKILL.md` по одному на агента
- **Gemini CLI** — extension + `SKILL.md`
- **Codex Official Skills** — official skills в `codex-skills/skills/`
- **Codex Curated Subagents** — curated `.toml` subagents в `codex-subagents/agents/`
- **Codex Legacy Skills** — legacy skills в `codex/skills/`
- **OpenCode** — `.md` agent files
- **OpenClaw** — workspace-структуры с `SOUL.md`, `AGENTS.md`, `IDENTITY.md`
- **Cursor** — `.mdc` rule files
- **Aider** — единый `CONVENTIONS.md`
- **Windsurf** — единый `.windsurfrules`

## Быстрая установка

```bash
# Автоустановка для найденных инструментов
./scripts/install.sh

# Отдельные варианты
./scripts/install.sh --tool claude-code
./scripts/install.sh --tool copilot
./scripts/install.sh --tool antigravity
./scripts/install.sh --tool gemini-cli
./scripts/install.sh --tool codex-all
```

### Рекомендуемый путь для Codex

```bash
./scripts/convert.sh --tool codex-all
./scripts/install.sh --tool codex-all
```

Это установит:

- official skills в `~/.agents/skills/`
- curated subagents в `${CODEX_HOME:-~/.codex}/agents/`

### Только official Codex skills

```bash
./scripts/convert.sh --tool codex-skills
./scripts/install.sh --tool codex-skills
```

### Только curated Codex subagents

```bash
./scripts/convert.sh --tool codex-subagents
./scripts/install.sh --tool codex-subagents
```

### Legacy Codex layout

```bash
./scripts/convert.sh --tool codex
./scripts/install.sh --tool codex
```

## Когда нужно запускать `convert.sh`

Если integration-файлы ещё не сгенерированы или устарели после изменения agent-файлов:

```bash
./scripts/convert.sh
```

## Что важно не переводить в форке

Даже в русской локализации лучше оставить на английском:

- команды shell;
- имена tool targets;
- пути;
- `SKILL.md`, `.toml`, `agency-*`, `codex-*`;
- технические идентификаторы.

Это сохраняет совместимость со скриптами и делает поведение форка предсказуемым.

## Codex-документация

- [codex-skills/README.ru.md](./codex-skills/README.ru.md)
- [codex-subagents/README.ru.md](./codex-subagents/README.ru.md)
- [codex/README.ru.md](./codex/README.ru.md)
