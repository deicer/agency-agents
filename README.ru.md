# 🎭 The Agency: библиотека ИИ-специалистов для реальных задач

> Русскоязычная вводная документация для форка `agency-agents`. Основной README на GitHub теперь тоже русский: команды, пути, имена skill/subagent и технические идентификаторы намеренно оставлены на английском ради совместимости.

[English README](./README.en.md)

---

## Что это такое

**The Agency** — это большая коллекция готовых agent/persona-инструкций для ИИ-инструментов.  
Каждый агент — это не отдельный процесс и не сервис, а хорошо проработанный markdown-файл с:

- ролью и специализацией;
- стилем общения и рабочими принципами;
- типовыми workflow;
- ожидаемыми deliverables;
- примерами того, как агент должен думать и действовать.

Проще всего воспринимать проект как **каталог готовых профессиональных ролей**: frontend, backend, security, product, marketing, testing, support и другие.

---

## Как этим пользоваться

Есть три базовых сценария:

### 1. Использовать как библиотеку ролей

Можно просто открыть нужный agent-файл, взять его инструкцию и адаптировать под свою задачу.

### 2. Подключить к поддерживаемому AI-инструменту

Репозиторий умеет конвертировать исходные agent-файлы в форматы разных инструментов и устанавливать их через скрипты.

Базовый сценарий:

```bash
# Сгенерировать integration-файлы
./scripts/convert.sh

# Установить их интерактивно
./scripts/install.sh
```

### 3. Использовать Codex

Для Codex теперь есть два режима:

- **official**: `codex-skills` + `codex-subagents`
- **legacy**: старый layout `codex`

Рекомендуемый вариант:

```bash
./scripts/convert.sh --tool codex-all
./scripts/install.sh --tool codex-all
```

Это устанавливает:

- official skills в `~/.agents/skills/`
- curated subagents в `${CODEX_HOME:-~/.codex}/agents/`

Подробнее см. в:

- [integrations/README.ru.md](./integrations/README.ru.md)
- [integrations/codex-skills/README.ru.md](./integrations/codex-skills/README.ru.md)
- [integrations/codex-subagents/README.ru.md](./integrations/codex-subagents/README.ru.md)
- [integrations/codex/README.ru.md](./integrations/codex/README.ru.md)

---

## Что уже есть в каталоге

Сейчас в проекте `156` agent-файлов, распределённых по крупным доменам:

- `engineering`
- `design`
- `testing`
- `product`
- `project-management`
- `marketing`
- `sales`
- `support`
- `specialized`
- `game-development`
- `spatial-computing`
- `academic`
- `paid-media`

Если тебе нужен в первую очередь технический набор для Codex, начни с таких ролей:

- Frontend Developer
- Backend Architect
- Code Reviewer
- Security Engineer
- Database Optimizer
- Technical Writer
- Software Architect
- SRE
- DevOps Automator
- API Tester
- Accessibility Auditor
- Performance Benchmarker
- Reality Checker
- MCP Builder
- Git Workflow Master

Именно этот набор сейчас лучше всего подходит и как skills, и как curated subagents.

---

## Поддерживаемые инструменты

Проект уже умеет работать с:

- Claude Code
- GitHub Copilot
- Antigravity
- Gemini CLI
- Codex
- OpenCode
- OpenClaw
- Cursor
- Aider
- Windsurf
- Qwen Code

Подробная русская сводка есть в [integrations/README.ru.md](./integrations/README.ru.md).

---

## Состояние русской локализации

Этот файл — старт локализации форка. На первом этапе переводятся:

- верхнеуровневая документация;
- integration docs;
- Codex-specific docs;
- затем — наиболее полезные технические agent-файлы.

Полный каталог ролей пока остаётся англоязычным, чтобы не замедлять развитие форка и не ломать совместимость со скриптами.

Важно: переводы самих agent-файлов не кладутся рядом с исходниками в `engineering/`, `testing/` и других agent-директориях. Скрипты `lint-agents.sh` и `convert.sh` подбирают там все `*.md`, поэтому русские companion-файлы должны жить отдельно.

Текущие переводы ролей собраны в [translations/ru/README.md](./translations/ru/README.md).
