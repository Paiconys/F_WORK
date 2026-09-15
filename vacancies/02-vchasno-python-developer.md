# 02 — VCHASNO GROUP · Python Developer

- Ссылка: https://djinni.co/jobs/778695-python-developer/
- Компания: VCHASNO GROUP / Zakupivli.Pro (product, Prozorro)
- Опыт: Python от 1 года · fulltime · product
- Обновлено: ~10 Sep 2026 (вакансия с 27 Oct 2025)

## Суть роли

Продуктовый backend: тендеры/аукционы. Стек: **Python, Pyramid, Aiohttp, Asyncio, Celery, Pytest**; Postgres, MongoDB, Redis, ElasticSearch, RabbitMQ, Minio; фронт React; деплой K8s / Docker / GitLab CI.

## Требования (важно)

- Python 1+ год
- Web / понимание микросервисов
- **asyncio обязательно**
- PostgreSQL; опыт Redis, Celery, RabbitMQ, MongoDB, ElasticSearch
- **Aiohttp обязательно**
- Тесты
- Git, Docker
- Глубоко разбирать задачу / предметную область

## Плюсом

- LLM, GraphQL, Kubernetes, интерес к AI / frontend

## Учить по блокам

| Требование вакансии | Блок(и) в F_WORK | Приоритет |
| --- | --- | --- |
| Python | [`python-basics`](../topics/python-basics/python-basics.md), [`python-oop`](../topics/python-oop/python-oop.md) | must |
| asyncio | [`python-async`](../topics/python-async/python-async.md) | must |
| Postgres / SQL / NoSQL идеи | [`databases`](../topics/databases/databases.md) | must |
| Redis | [`caching`](../topics/caching/caching.md), [`realtime`](../topics/realtime/realtime.md) (роли Redis) | must |
| Celery / очереди / broker | [`queues`](../topics/queues/queues.md) | must |
| REST / API | [`rest-drf`](../topics/rest-drf/rest-drf.md) | must |
| Тесты (pytest) | [`python-testing`](../topics/python-testing/python-testing.md) | must |
| Git | [`git`](../topics/git/git.md) | must |
| Docker | [`docker-infra`](../topics/docker-infra/docker-infra.md) | must |
| Практики / архитектура | [`practices`](../topics/practices/practices.md) | should |
| Frontend SPA (плюс) | [`frontend`](../topics/frontend/frontend.md) | nice |
| Auth / security API | [`auth`](../topics/auth/auth.md), [`security`](../topics/security/security.md) | should |

## Gap (нет отдельного блока)

- **Aiohttp / Pyramid** (у нас Django-ориентированные блоки)
- **RabbitMQ** (есть идея очередей через Celery)
- **ElasticSearch / MongoDB** детально
- **GraphQL**, **Kubernetes**, **GitLab CI**
- LLM-интеграции

## План повторения (коротко)

1. `python-async` до уверенного рассказа asyncio
2. `databases` + `caching` + `queues`
3. `rest-drf` + `python-testing` + `docker-infra` + `git`
4. Снаружи: aiohttp hello-service + Celery+Redis demo
