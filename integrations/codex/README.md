# Codex Legacy Skills

Russian translation starter: [README.ru.md](./README.ru.md)

Legacy Codex integration packages every Agency agent as a Codex skill
(`SKILL.md` per agent) and installs them to `${CODEX_HOME:-~/.codex}/skills/`.

Use this mode only if you already rely on the older Codex layout. For new
setups, prefer `codex-all`, `codex-skills`, and `codex-subagents`.

## Install

```bash
# Generate legacy Codex integration files
./scripts/convert.sh --tool codex

# Install generated skills to the legacy Codex path
./scripts/install.sh --tool codex
```

## Activate a Skill

In Codex, reference an installed skill by name:

```text
Use the $agency-frontend-developer skill to help me build this UI.
```

## Generated Structure

```text
integrations/codex/skills/
  agency-frontend-developer/SKILL.md
  agency-backend-architect/SKILL.md
  agency-reality-checker/SKILL.md
  ...
```
