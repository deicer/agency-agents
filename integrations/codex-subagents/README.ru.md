# Codex Curated Subagents

Curated Codex subagents — это сфокусированные `.toml`-субагенты для Codex,
собранные из самых практичных ролей `The Agency`.

Они устанавливаются в `${CODEX_HOME:-~/.codex}/agents/`.

[English version](./README.md)

В отличие от full skills, эти subagents намеренно более узкие:

- у них чёткая зона ответственности;
- предсказуемый sandbox;
- короткие operational instructions;
- удобная модель для делегирования.

## Установка

```bash
# Сгенерировать curated Codex subagents
./scripts/convert.sh --tool codex-subagents

# Установить их в ~/.codex/agents (или $CODEX_HOME/agents)
./scripts/install.sh --tool codex-subagents
```

Рекомендуемый combined-вариант вместе с official skills:

```bash
./scripts/convert.sh --tool codex-all
./scripts/install.sh --tool codex-all
```

## Структура generated-файлов

```text
integrations/codex-subagents/agents/
  agency-code-reviewer.toml
  agency-security-engineer.toml
  agency-frontend-developer.toml
  ...
```

## Curated роли

- `agency-code-reviewer` — review PR на корректность, регрессии и недостающие тесты
- `agency-security-engineer` — security review для auth, trust boundaries и unsafe defaults
- `agency-frontend-developer` — сфокусированная UI-реализация
- `agency-backend-architect` — review API, data flow и design boundaries
- `agency-technical-writer` — README, migration notes и usage docs
- `agency-database-optimizer` — review schema, indexes и queries
- `agency-sre` — operability и production-readiness review
- `agency-devops-automator` — CI/CD и deployment automation
- `agency-api-tester` — API tests и contract checks
- `agency-accessibility-auditor` — accessibility review
- `agency-performance-benchmarker` — benchmark/profiling задачи
- `agency-reality-checker` — release-readiness и evidence-based verification
- `agency-mcp-builder` — MCP server/tool integration work
- `agency-git-workflow-master` — review git/release flow
- `agency-software-architect` — architecture/trade-off review

## Как использовать

Проси Codex делегировать задачу конкретному субагенту, когда нужна узкая и специализированная роль.

Примеры:

```text
Use the agency-code-reviewer subagent to review this branch for regressions.
```

```text
Use the agency-frontend-developer subagent to implement the small UI fix.
```

Когда рядом установлены official skills, установленный subagent также получает
`skills.config`-ссылку на соответствующий Agency skill. Это позволяет держать
subagent компактным, а подробный playbook — в skill.
