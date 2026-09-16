# English (grammar for interviews)

Блок для B1–B2: таблицы + **зачем** + короткие **prompts** (допиши ответ сам).
Не теория ради теории — формулировки, которые звучат на техсобесе.

---

## Present Simple / Continuous

| | Present Simple | Present Continuous |
| --- | --- | --- |
| Форма | `V` / `V-s` | `am/is/are + V-ing` |
| Когда | факты, привычки, расписание | сейчас / временный процесс |
| Сигналы | always, usually, every day | now, at the moment, currently |
| Пример | I **work** with Django. | I **am working** on the auth module. |

**Зачем:** Simple — про стек и опыт в целом; Continuous — про текущую задачу.

**Prompts**
1. What do you usually do at work? → …
2. What are you working on right now? → …

---

## Past Simple / Continuous

| | Past Simple | Past Continuous |
| --- | --- | --- |
| Форма | `V2` / `ed` | `was/were + V-ing` |
| Когда | законченное действие в прошлом | фон / процесс в тот момент |
| Сигналы | yesterday, last year, in 2024 | while, when, at 5 pm yesterday |
| Пример | We **deployed** to prod. | I **was debugging** when the alert fired. |

**Зачем:** Simple — факты из опыта («сделал X»); Continuous — история бага/инцидента.

**Prompts**
1. Tell me about a bug you fixed. → …
2. What were you doing when the service went down? → …

---

## Present Perfect / Past Simple

| | Present Perfect | Past Simple |
| --- | --- | --- |
| Форма | `have/has + V3` | `V2` |
| Когда | опыт / связь с сейчас / результат важен | конкретное время в прошлом |
| Сигналы | ever, never, already, yet, so far | yesterday, in 2023, last week |
| Пример | I **have used** Redis. | I **used** Redis in that project in 2025. |

**Зачем:** Perfect — «есть опыт»; Simple — «когда именно / в каком проекте».

**Prompts**
1. Have you ever worked with Docker? → …
2. When did you last write a migration? → …

---

## Present Perfect Continuous

| | Форма | Когда | Пример |
| --- | --- | --- | --- |
| Present Perfect Continuous | `have/has been + V-ing` | длительность до сейчас | I **have been learning** asyncio for two months. |

**Зачем:** подчеркнуть процесс обучения / длительную работу над фичей.

**Prompt:** How long have you been preparing for interviews? → …

---

## Past Perfect

| | Форма | Когда | Пример |
| --- | --- | --- | --- |
| Past Perfect | `had + V3` | раньше другого прошлого | The job **had failed** before we noticed. |

**Зачем:** порядок событий в postmortem («сначала A, потом B»).

**Prompt:** Explain an incident using before/after. → …

---

## Future: will / going to / Present Continuous

| | will | going to | Present Continuous (future) |
| --- | --- | --- | --- |
| Когда | решение сейчас / обещание / прогноз | план / намерение | договорённость в календаре |
| Пример | I **will** check the logs. | We **are going to** refactor that. | I **am meeting** the team at 3. |

**Зачем:** на собесе про планы и next steps.

**Prompt:** What will you do if the API is slow? → …

---

## Active / Passive Voice

| | Active | Passive |
| --- | --- | --- |
| Форма | Subject + Verb + Object | Object + `be + V3` (+ by …) |
| Фокус | кто сделал | что сделали с объектом |
| Пример | We **deployed** the service. | The service **was deployed**. |
| Пример 2 | Redis **stores** the cache. | The cache **is stored** in Redis. |

**Когда Passive уместен**
- процесс важнее автора: *The request is validated…*
- неизвестный автор: *The data was corrupted.*
- формальный стиль (доки, постмортем)

**Когда лучше Active**
- рассказ про свой вклад: *I implemented…* (не *It was implemented by me* без нужды)

**Таблица по временам (Passive)**

| Время | Passive |
| --- | --- |
| Present Simple | is/are + V3 — *is cached* |
| Past Simple | was/were + V3 — *was deleted* |
| Present Perfect | has/have been + V3 — *has been fixed* |
| Modal | can/must be + V3 — *must be authenticated* |

**Prompts**
1. Rewrite actively: “The token is verified by the middleware.” → …
2. Rewrite passively: “Celery sends the email.” → …

---

## Conditionals (0–3)

| Тип | Форма | Когда | Пример |
| --- | --- | --- | --- |
| 0 | If + Present, Present | всегда правда | If Redis is down, the cache **misses**. |
| 1 | If + Present, will | реальный future | If the test fails, we **will** block the merge. |
| 2 | If + Past, would | гипотеза сейчас | If I **had** more time, I **would** add metrics. |
| 3 | If + Past Perfect, would have + V3 | жалость о прошлом | If we **had** tested it, we **would have** caught the bug. |

**Зачем:** дизайн-решения и разбор ошибок без «ломаного» if.

**Prompt:** If the database is slow, what will you check first? → …

---

## Modals

| Modal | Зачем | Пример |
| --- | --- | --- |
| can / can't | умение / возможность | I **can** explain N+1. |
| must / have to | обязанность (must — сильнее/правило) | You **must** validate on the server. |
| should / shouldn't | совет | We **should** add an index. |
| might / may | вероятность | It **might** be a race condition. |
| would | гипотеза / вежливость | I **would** start with the logs. |

**Prompt:** What should we do before a production migration? → …

---

## Articles (a / an / the) — кратко

| | Когда | Пример |
| --- | --- | --- |
| a / an | один из многих, впервые | a bug, an API |
| the | конкретный / единственный / уже известный | the bug we found, the database |
| zero | общее / языки / большинство абстракций | Python, Docker, production (часто) |

**Зачем:** меньше «student English» на собесе.

**Prompt:** Fix articles: “I fixed bug in the Redis.” → …

---

## Countable / Uncountable (частые на IT)

| Countable | Uncountable |
| --- | --- |
| a bug, two services | information, advice, code (часто), traffic |
| many / few | much / little |
| a piece of advice | — |

**Prompt:** much or many — “___ requests per second”? → …

---

## Comparatives (коротко)

| | Форма | Пример |
| --- | --- | --- |
| short adj | -er / the -est | faster, the fastest |
| long adj | more / the most | more reliable |
| equal | as … as | as fast as Redis |
| irregular | better, worse | better latency |

**Prompt:** Postgres is ___ than SQLite for concurrency. → …

---

## Reported speech (для историй)

| Direct | Reported |
| --- | --- |
| “We need a fix.” | He said we **needed** a fix. |
| “I will deploy.” | She said she **would** deploy. |

**Зачем:** пересказ обсуждения в команде.

---

## Useful interview chunks

| Цель | Фраза |
| --- | --- |
| Начать ответ | So, basically… / In short… |
| Уточнить | Do you mean X or Y? |
| Не уверен | I’m not sure, but I’d check… |
| Опыт | I’ve worked with… / In my last project… |
| Trade-off | The trade-off is… |
| Инцидент | First we… then we… finally we… |
| Просьба повторить | Could you repeat the last part? |

**Prompts (ответь вслух 30–60 сек)**
1. Explain what a REST API is.
2. Explain N+1 and how to fix it.
3. Describe a production bug using Past Simple + Past Perfect.
4. Say what you are working on using Present Continuous.
5. Give advice about secrets in git using *should/must*.

---

## Quick self-check

| Хочу сказать | Время / конструкция |
| --- | --- |
| Мой обычный стек | Present Simple |
| Чем занят сейчас | Present Continuous |
| Есть опыт с X | Present Perfect |
| Конкретный проект в 2025 | Past Simple |
| План на фикс | will / going to |
| Процесс важнее автора | Passive |
| Гипотеза | would / 2nd conditional |
