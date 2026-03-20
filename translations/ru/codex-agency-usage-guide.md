# Agency Agents для Codex: быстрый справочник

Этот документ собирает в одном месте:

- разницу между `skills` и `subagents`;
- самые полезные роли для повседневной работы;
- список всех установленных `agency-*` субагентов;
- готовые шаблоны промптов на русском.

Документ ориентирован на установленную у тебя конфигурацию:

- skills в `~/.agents/skills`
- subagents в `~/.codex/agents`

## Что у тебя установлено

Сейчас установлено:

- `156` agency skills
- `15` curated subagents

Примеры реальных путей:

- `C:\Users\deicer\.agents\skills\agency-frontend-developer\SKILL.md`
- `C:\Users\deicer\.codex\agents\agency-code-reviewer.toml`

## Skills и Subagents: в чём разница

### Skills

Используй `skills`, когда хочешь подтянуть роль как набор инструкций и контекста для текущего основного агента.

Типовая форма:

```text
Используй скилл $agency-frontend-developer, чтобы помочь мне собрать адаптивную страницу настроек на React.
```

Когда это удобно:

- нужна экспертная роль, но без отдельного исполнителя;
- хочешь просто усилить текущий ответ;
- задача не требует явного делегирования.

### Subagents

Используй `subagents`, когда хочешь отдельного узкого исполнителя или проверяющего.

Типовая форма:

```text
Пожалуйста, используй субагента agency-code-reviewer, чтобы проверить мои изменения.
```

Когда это удобно:

- нужен отдельный reviewer или auditor;
- задача хорошо делегируется;
- хочешь получить более узкую, специализированную точку зрения.

## Топ-7 самых полезных ролей на каждый день

Если не хочется держать в голове весь список, вот 7 самых практичных.

### 1. `agency-code-reviewer`

Лучший общий проверяющий.

Вызывай когда нужно:

- проверить PR;
- найти регрессии;
- понять, где не хватает тестов;
- получить сильный review по корректности.

Пример:

```text
Пожалуйста, используй субагента agency-code-reviewer, чтобы проверить мои текущие изменения на корректность, регрессии и недостающие тесты.
```

### 2. `agency-frontend-developer`

Самая полезная роль для UI, экранов и компонентной работы.

Вызывай когда нужно:

- собрать страницу;
- улучшить UX;
- сделать responsive;
- поправить accessibility в интерфейсе.

Пример:

```text
Используй скилл $agency-frontend-developer, чтобы помочь мне сделать адаптивную и доступную страницу настроек на React.
```

### 3. `agency-backend-architect`

Подходит для API, сервисов, схем данных и backend design.

Вызывай когда нужно:

- проектировать API;
- решать, как разложить систему на сервисы;
- выбрать структуру базы;
- продумать масштабирование.

Пример:

```text
Используй скилл $agency-backend-architect, чтобы спроектировать API и схему базы данных для multi-tenant SaaS.
```

### 4. `agency-security-engineer`

Главный выбор для security-аудита.

Вызывай когда нужно:

- проверить auth;
- найти уязвимости;
- оценить секреты, permissions и attack surface;
- сделать security review фичи.

Пример:

```text
Пожалуйста, используй субагента agency-security-engineer, чтобы проверить этот auth flow на уязвимости и ошибки в access control.
```

### 5. `agency-reality-checker`

Жёсткий финальный проверяющий, который не верит красивым словам без evidence.

Вызывай когда нужно:

- честно оценить readiness к продакшену;
- понять, действительно ли всё готово;
- получить строгую итоговую оценку.

Пример:

```text
Пожалуйста, используй субагента agency-reality-checker, чтобы строго оценить, действительно ли эта фича готова к продакшену.
```

### 6. `agency-mcp-builder`

Практически обязательный, если работаешь с MCP servers, tools и integrations.

Вызывай когда нужно:

- проектировать MCP server;
- продумать tools/resources/prompts;
- реализовать интеграцию к внутреннему API или базе.

Пример:

```text
Пожалуйста, используй субагента agency-mcp-builder, чтобы помочь спроектировать MCP server для этого внутреннего API.
```

### 7. `agency-git-workflow-master`

Очень полезен для веток, истории коммитов и подготовки merge.

Вызывай когда нужно:

- привести ветку в порядок;
- почистить историю;
- безопасно сделать rebase;
- понять, как лучше слить изменения.

Пример:

```text
Используй скилл $agency-git-workflow-master, чтобы помочь мне аккуратно почистить ветку и подготовить безопасный merge.
```

## Все установленные субагенты

Ниже список всех 15 установленных `agency-*` subagents и когда какой вызывать.

### `agency-accessibility-auditor`

Используй для:

- WCAG-проверки;
- keyboard navigation;
- screen reader compatibility;
- accessibility audit.

### `agency-api-tester`

Используй для:

- проверки API;
- contract validation;
- auth / rate limit / edge cases;
- API performance testing.

### `agency-backend-architect`

Используй для:

- API design;
- схем данных;
- service architecture;
- backend scaling.

### `agency-code-reviewer`

Используй для:

- review изменений;
- поиска регрессий;
- проверки корректности;
- оценки покрытия тестами.

### `agency-database-optimizer`

Используй для:

- SQL и индексов;
- slow queries;
- query plans;
- миграций и schema design.

### `agency-devops-automator`

Используй для:

- CI/CD;
- Docker / Kubernetes;
- IaC;
- deployment automation и infra workflows.

### `agency-frontend-developer`

Используй для:

- UI-задач;
- экранов и компонент;
- responsive и accessibility;
- frontend implementation.

### `agency-git-workflow-master`

Используй для:

- cleanup веток;
- rebase и merge strategy;
- conventional commits;
- безопасного Git workflow.

### `agency-mcp-builder`

Используй для:

- MCP servers;
- tools / resources / prompts;
- проектирования интеграций;
- реализации новых MCP capabilities.

### `agency-performance-benchmarker`

Используй для:

- benchmark;
- bottleneck hunting;
- performance analysis;
- SLA и load testing.

### `agency-reality-checker`

Используй для:

- итоговой строгой проверки качества;
- production readiness assessment;
- проверки claims against evidence;
- честной финальной оценки.

### `agency-security-engineer`

Используй для:

- security review;
- auth и access control;
- vulnerability assessment;
- threat modeling.

### `agency-software-architect`

Используй для:

- high-level architecture;
- DDD;
- bounded contexts;
- ADR и системного дизайна.

### `agency-sre`

Используй для:

- reliability;
- observability;
- SLO / error budgets;
- production stability и incident readiness.

### `agency-technical-writer`

Используй для:

- README;
- onboarding docs;
- guides и tutorials;
- API documentation.

## Готовые шаблоны промптов

Ниже короткие готовые формулировки, которые можно просто вставлять в Codex.

### UI и frontend

```text
Используй скилл $agency-frontend-developer, чтобы помочь мне собрать адаптивную страницу настроек на React с хорошей доступностью.
```

### Backend и архитектура

```text
Используй скилл $agency-backend-architect, чтобы спроектировать масштабируемый API и схему базы данных для multi-tenant SaaS.
```

### Документация

```text
Используй скилл $agency-technical-writer, чтобы переписать этот README так, чтобы новый разработчик мог стартовать меньше чем за 5 минут.
```

### Code review

```text
Пожалуйста, используй субагента agency-code-reviewer, чтобы проверить мои текущие изменения на корректность, регрессии и недостающие тесты.
```

### Security

```text
Пожалуйста, используй субагента agency-security-engineer, чтобы проверить этот auth flow на уязвимости и ошибки в access control.
```

### MCP

```text
Пожалуйста, используй субагента agency-mcp-builder, чтобы помочь спроектировать MCP server для этого внутреннего API.
```

### Production readiness

```text
Пожалуйста, используй субагента agency-reality-checker, чтобы строго оценить, действительно ли эта фича готова к продакшену.
```

### База данных

```text
Используй скилл $agency-database-optimizer, чтобы проанализировать эти SQL-запросы и предложить улучшения по индексам.
```

### Git и merge

```text
Используй скилл $agency-git-workflow-master, чтобы помочь мне привести ветку в порядок и подготовить безопасный merge.
```

### Performance

```text
Пожалуйста, используй субагента agency-performance-benchmarker, чтобы оценить вероятные bottleneck'и в этом сервисе.
```

## Простое правило выбора

- `Используй скилл $agency-...`
  Когда хочешь подтянуть роль как набор инструкций для текущего агента.

- `Используй субагента agency-...`
  Когда хочешь отдельного узкого исполнителя, reviewer или auditor.

## Рекомендуемый повседневный набор

Если нужен совсем короткий набор “по умолчанию”, держи в голове эти роли:

- `agency-code-reviewer`
- `agency-frontend-developer`
- `agency-backend-architect`
- `agency-security-engineer`
- `agency-reality-checker`
- `agency-mcp-builder`
- `agency-git-workflow-master`

Этого уже хватает, чтобы закрывать большую часть повседневной работы: реализацию, review, безопасность, интеграции, выпуск и финальную проверку качества.
