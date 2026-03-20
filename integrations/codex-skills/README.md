# Codex Official Skills

Official Codex skill integration packages every Agency agent as a skill
(`SKILL.md` per agent) and installs them to `~/.agents/skills/`.

This is the recommended Codex skill layout for new installs.

## Install

```bash
# Generate official Codex skills
./scripts/convert.sh --tool codex-skills

# Install them to ~/.agents/skills
./scripts/install.sh --tool codex-skills
```

## Activate a Skill

In Codex, reference the skill by name:

```text
Use the $agency-frontend-developer skill to help me build this UI.
```

```text
Use the $agency-reality-checker skill to verify this is production-ready.
```

## Generated Structure

```text
integrations/codex-skills/skills/
  agency-frontend-developer/SKILL.md
  agency-backend-architect/SKILL.md
  agency-reality-checker/SKILL.md
  ...
```

## Recommended Pairing

If you also want Codex-native delegation, install curated subagents too:

```bash
./scripts/convert.sh --tool codex-all
./scripts/install.sh --tool codex-all
```
