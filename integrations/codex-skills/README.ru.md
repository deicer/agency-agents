# Codex Official Skills

Official Codex skills упаковывают каждого агента в отдельный skill
(`SKILL.md`) и устанавливаются в `~/.agents/skills/`.

[English version](./README.md)

Это рекомендуемый layout для новых установок Codex.

## Установка

```bash
# Сгенерировать official Codex skills
./scripts/convert.sh --tool codex-skills

# Установить их в ~/.agents/skills
./scripts/install.sh --tool codex-skills
```

## Как вызывать skill

В Codex можно явно сослаться на skill по имени:

```text
Use the $agency-frontend-developer skill to help me build this UI.
```

```text
Use the $agency-reality-checker skill to verify this is production-ready.
```

## Структура generated-файлов

```text
integrations/codex-skills/skills/
  agency-frontend-developer/SKILL.md
  agency-backend-architect/SKILL.md
  agency-reality-checker/SKILL.md
  ...
```

## Рекомендуемое сочетание

Если ты хочешь не только skills, но и Codex-native delegation через subagents:

```bash
./scripts/convert.sh --tool codex-all
./scripts/install.sh --tool codex-all
```
