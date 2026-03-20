# Codex Curated Subagents

Russian translation starter: [README.ru.md](./README.ru.md)

Curated Codex subagents package the most practical Agency roles as focused
Codex subagents (`.toml` files) and install them to
`${CODEX_HOME:-~/.codex}/agents/`.

These subagents are intentionally narrower than the full skills. They are
designed for targeted delegation, clear ownership, and predictable sandboxing.

## Install

```bash
# Generate curated Codex subagents
./scripts/convert.sh --tool codex-subagents

# Install them to ~/.codex/agents (or $CODEX_HOME/agents)
./scripts/install.sh --tool codex-subagents
```

Recommended combined install with official skills:

```bash
./scripts/convert.sh --tool codex-all
./scripts/install.sh --tool codex-all
```

## Generated Structure

```text
integrations/codex-subagents/agents/
  agency-code-reviewer.toml
  agency-security-engineer.toml
  agency-frontend-developer.toml
  ...
```

## Curated Roles

- `agency-code-reviewer` — PR review for correctness, regressions, and missing tests
- `agency-security-engineer` — security review for auth, trust boundaries, and unsafe defaults
- `agency-frontend-developer` — focused UI implementation work
- `agency-backend-architect` — API/data-flow/design review
- `agency-technical-writer` — README, migration, and usage docs
- `agency-database-optimizer` — schema/query/index review
- `agency-sre` — operability and production-readiness review
- `agency-devops-automator` — CI/CD and deployment automation changes
- `agency-api-tester` — API-focused test additions and contract checks
- `agency-accessibility-auditor` — accessibility review
- `agency-performance-benchmarker` — benchmark and profiling tasks
- `agency-reality-checker` — release-readiness and evidence-based verification
- `agency-mcp-builder` — MCP server and tool-integration work
- `agency-git-workflow-master` — git/release-flow review
- `agency-software-architect` — boundary/trade-off design review

## How to Use

Ask Codex to delegate to a named subagent when you want narrow, role-specific
help. Examples:

```text
Use the agency-code-reviewer subagent to review this branch for regressions.
```

```text
Use the agency-frontend-developer subagent to implement the small UI fix.
```

When official skills are installed alongside the subagents, each installed
subagent also receives a `skills.config` link to its matching Agency skill so
the detailed playbook remains available without making the subagent bloated.
