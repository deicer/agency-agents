# Русские переводы ролей

Это безопасное дерево русской локализации для agent-файлов из `agency-agents`.

Почему переводы лежат здесь, а не рядом с оригиналами:

- `scripts/lint-agents.sh` и `scripts/convert.sh` сканируют agent-директории и подбирают все `*.md`;
- если положить `*.ru.md` рядом с исходными файлами, переводы начнут считаться отдельными агентами;
- это сломает подсчёты, lint и generated integrations.

Поэтому исходные agent-файлы остаются нетронутыми, а русские версии складываются в отдельное mirrored-дерево.

## Принципы локализации

- сохраняем англоязычные slug'и, имена исходных файлов и технические идентификаторы;
- переводим persona, mission, workflow, deliverables и explanatory prose;
- команды, пути, код и config-примеры оставляем на английском;
- `name` обычно сохраняется на английском для удобного сопоставления с оригиналом.

## P0: переведённые роли

Engineering:

- [engineering/engineering-backend-architect.md](./engineering/engineering-backend-architect.md)
- [engineering/engineering-frontend-developer.md](./engineering/engineering-frontend-developer.md)
- [engineering/engineering-code-reviewer.md](./engineering/engineering-code-reviewer.md)
- [engineering/engineering-database-optimizer.md](./engineering/engineering-database-optimizer.md)
- [engineering/engineering-security-engineer.md](./engineering/engineering-security-engineer.md)
- [engineering/engineering-software-architect.md](./engineering/engineering-software-architect.md)
- [engineering/engineering-sre.md](./engineering/engineering-sre.md)
- [engineering/engineering-technical-writer.md](./engineering/engineering-technical-writer.md)
- [engineering/engineering-git-workflow-master.md](./engineering/engineering-git-workflow-master.md)
- [engineering/engineering-devops-automator.md](./engineering/engineering-devops-automator.md)

Specialized:

- [specialized/specialized-mcp-builder.md](./specialized/specialized-mcp-builder.md)

Testing:

- [testing/testing-api-tester.md](./testing/testing-api-tester.md)
- [testing/testing-accessibility-auditor.md](./testing/testing-accessibility-auditor.md)
- [testing/testing-performance-benchmarker.md](./testing/testing-performance-benchmarker.md)
- [testing/testing-reality-checker.md](./testing/testing-reality-checker.md)

Следующий шаг после этого минимума:
- `remaining-engineering`
- `remaining-testing`
- `design`
- `product`
- `project-management`
- `support`
