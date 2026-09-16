# F_WORK — теория к техсобесу

Один **блок темы** = один файл `{тема}/{тема}.md` (все вопросы подряд).
Отдельно — выгрузки с реальных собесов в `interviews/`.

Каталог блоков и вопросов без ответов: [`questions.md`](./questions.md).

Вакансии → что учить: [`vacancies/`](./vacancies/).

## Темы

- [`python-basics`](./topics/python-basics/python-basics.md) — Python basics (23)
- [`python-oop`](./topics/python-oop/python-oop.md) — Python — ООП (13)
- [`python-async`](./topics/python-async/python-async.md) — Python — async / GIL / параллелизм (7)
- [`python-testing`](./topics/python-testing/python-testing.md) — Python — тестирование (4)
- [`databases`](./topics/databases/databases.md) — Базы данных и ORM (18)
- [`django`](./topics/django/django.md) — Django (16)
- [`fastapi`](./topics/fastapi/fastapi.md) — FastAPI (8)
- [`aiohttp`](./topics/aiohttp/aiohttp.md) — aiohttp (6)
- [`rest-drf`](./topics/rest-drf/rest-drf.md) — REST / DRF (10)
- [`security`](./topics/security/security.md) — Безопасность веб (6)
- [`auth`](./topics/auth/auth.md) — Аутентификация и авторизация (3)
- [`caching`](./topics/caching/caching.md) — Кэш (3)
- [`queues`](./topics/queues/queues.md) — Очереди и фоновые задачи (2)
- [`realtime`](./topics/realtime/realtime.md) — Realtime: WebSocket / Channels (8)
- [`frontend`](./topics/frontend/frontend.md) — Frontend (3)
- [`docker-infra`](./topics/docker-infra/docker-infra.md) — Docker и инфраструктура (6)
- [`git`](./topics/git/git.md) — Git (4)
- [`practices`](./topics/practices/practices.md) — Практики (SOLID, паттерны) (2)
- [`ai-tools`](./topics/ai-tools/ai-tools.md) — AI tools (для разработки) (6)
- [`english`](./topics/english/english.md) — English (времена, active/passive, prompts)

## Вакансии

- [`vacancies/`](./vacancies/) — вакансия → требования → блоки; новые технологии сначала в `topics/`/`questions.md`

## Собесы

- [`interview-01`](./interviews/interview-01.md) — Codeshare 14 Sep 2026 (mutable default, MRO, late binding)

## Запуск примеров

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-examples.txt

python topics/python-oop/examples/mro_demo.py
python interviews/interview-01-examples/mutable_default.py
```

## Git

Чтобы Cursor не попадал в `Co-authored-by` коммитов:

```bash
git config core.hooksPath .githooks
```

## Правила

1. Сначала сверься с [`questions.md`](./questions.md) (блоки → вопросы), потом пиши ответ в теме.
2. Тема = один md-файл со всеми вопросами блока.
3. Новые собесы клади в `interviews/interview-02.md`, `interview-03.md`, …
4. Примеры кода — в `examples/` рядом с темой или в `interviews/interview-NN-examples/`.
