# Codex Legacy Skills

Legacy-интеграция для Codex упаковывает каждого агента в skill
(`SKILL.md` на одного агента) и устанавливает их в
`${CODEX_HOME:-~/.codex}/skills/`.

[English version](./README.md)

Используй этот режим только если тебе нужен старый layout. Для новых установок лучше использовать:

- `codex-all`
- `codex-skills`
- `codex-subagents`

## Установка

```bash
# Сгенерировать legacy Codex integration files
./scripts/convert.sh --tool codex

# Установить legacy skills
./scripts/install.sh --tool codex
```

## Активация skill

В Codex можно ссылаться на установленный skill по имени:

```text
Use the $agency-frontend-developer skill to help me build this UI.
```

## Структура generated-файлов

```text
integrations/codex/skills/
  agency-frontend-developer/SKILL.md
  agency-backend-architect/SKILL.md
  agency-reality-checker/SKILL.md
  ...
```
