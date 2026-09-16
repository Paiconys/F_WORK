# Questions

Каталог блоков и вопросов **без ответов** — чтобы не дублировать при добавлении.
Ответы: `topics/<блок>/<блок>.md`. Собесы: `interviews/`. Вакансии: `vacancies/`.

Новые технологии из вакансий → сначала строка здесь и блок в `topics/`, потом ссылка из файла вакансии.

---

## Блоки (порядок)

1. `python-basics` — Python basics
2. `python-oop` — Python — ООП
3. `python-async` — Python — async / GIL / параллелизм
4. `python-testing` — Python — тестирование
5. `databases` — Базы данных и ORM
6. `django` — Django
7. `fastapi` — FastAPI
8. `aiohttp` — aiohttp
9. `rest-drf` — REST / DRF
10. `security` — Безопасность веб
11. `auth` — Аутентификация и авторизация
12. `caching` — Кэш
13. `queues` — Очереди и фоновые задачи
14. `realtime` — Realtime: WebSocket / Channels
15. `frontend` — Frontend
16. `docker-infra` — Docker и инфраструктура
17. `git` — Git
18. `practices` — Практики (SOLID, паттерны)
19. `ai-tools` — AI tools (для разработки)
20. `english` — English (времена, active/passive, prompts)

Новый блок: допиши строку сюда → создай `topics/<имя>/<имя>.md` → добавь секцию вопросов ниже.

---

## Вопросы по блокам

### `python-basics`

- Какие бывают типы данных в Python
- Какие типы данных относятся к изменяемым, какие нет
- Чем отличаются операторы == и is
- Что такое глубокая и поверхностная копия? Зачем нужны? Как их сделать?
- Как в Python передаются аргументы в функцию (изменяемые и неизменяемые)
- Что такое args и kwargs? Чем представлены?
- что такое lambda функция. кейсы применения
- Что такое аннотации типов, зачем они нужны, когда выполняются
- Что такое тернарный оператор, как записывается
- list comprehension / generator expression — отличия
- Что такое генератор? Как написать на Python генератор?
- Что такое итератор? Что такое итерируемый объект?
- `__str__` / `__repr__` — зачем
- dataclass — что это, зачем
- Exceptions: как обрабатывать, зачем свои исключения
- Что такое context manager (`with`)? Зачем нужен?
- `if __name__ == "__main__"`
- Poetry
- Абсолютные vs относительные импорты
- Модуль и пакет
- Что такое виртуальное окружение? Зачем оно нужно? Какие инструменты для этого используются?
- Как оценивается сложность алгоритмов и почему? Что такое Big O notation?
- Какая сложность основных операций в коллекциях?

Ответы: [`topics/python-basics/python-basics.md`](./topics/python-basics/python-basics.md)

### `python-oop`

- OOP — как применяли в моделях/сериализаторах
- В Python нет модификаторов доступа… public, private и protected
- Зачем нужен метод super в классе?
- Как в python реализуются методы объекта, класса и статические методы? Чем они отличаются?
- Какие базовые принципы ООП?
- Чем отличается атрибут класса от атрибута объекта?
- Что такое diamond problem? Что такое MRO? Чем отличается MRO2 от MRO3? Зачем оно нужно?
- Что такое self в классах?
- Что такое абстрактный класс? … в Python
- Что такое декораторы? … простой и с аргументом
- Что такое метаклассы? …
- Что такое миксины?
- Что такое ООП?

Ответы: [`topics/python-oop/python-oop.md`](./topics/python-oop/python-oop.md)

### `python-async`

- Asynchronous programming
- Flask / Tornado
- threading vs multiprocessing vs asyncio (когда что)
- Какие есть типы асинхронного выполнения?
- Что такое async и await?
- Что такое GIL, какие проблемы он решает, плюсы и минусы
- Что такое корутина?

Ответы: [`topics/python-async/python-async.md`](./topics/python-async/python-async.md)

### `python-testing`

- Pytest
- Unittest
- Какие модули в Python есть для тестирования? Какие отличия, плюсы и минусы?
- Что такое mock? Зачем нужен?

Ответы: [`topics/python-testing/python-testing.md`](./topics/python-testing/python-testing.md)

### `databases`

- ACID
- connection pooling
- denormalization vs normalization
- EXPLAIN / как понять медленный запрос
- on_delete: CASCADE / SET_NULL / PROTECT
- PK и FK
- unique / constraints
- Зачем нужны индексы?
- Зачем нужны триггеры?
- Какие NoSQL базы данных знаешь… плюсы и минусы
- Какие SQL базы данных знаешь… плюсы и минусы
- Типы связей. Many-to-many
- Уровни изолированности транзакции
- Что такое транзакция?
- JOIN / что делает ORM вместо JOIN
- ORM: filter/get, ленивость QuerySet
- SQLAlchemy
- что такое ORM. С какими работал?

Ответы: [`topics/databases/databases.md`](./topics/databases/databases.md)

### `django`

- `get_queryset` vs атрибут `queryset`
- admin — зачем
- blank vs null
- Django + Django ORM
- ForeignKey, on_delete, related_name
- HttpRequest / HttpResponse
- management commands (`migrate`, `shell`)
- MTV / что происходит с request
- N+1, select_related / prefetch_related
- Pillow
- settings: DEBUG, SECRET_KEY, ALLOWED_HOSTS
- signals (хотя бы «что это»)
- static vs media
- urlpatterns / path
- миграции
- Миграции на проде

Ответы: [`topics/django/django.md`](./topics/django/django.md)

### `fastapi`

- Что такое FastAPI и зачем он
- ASGI и почему FastAPI быстрый
- Path / Query параметры и type hints
- Pydantic-модели для body
- Depends — что это
- async def vs def в хендлерах
- Автодокументация OpenAPI
- FastAPI vs Django/DRF — когда что

Ответы: [`topics/fastapi/fastapi.md`](./topics/fastapi/fastapi.md)

### `aiohttp`

- Что такое aiohttp
- Client vs Server API
- Application, Router, Request/Response
- Зачем ClientSession
- aiohttp vs FastAPI / asyncio
- Типичные ошибки на собесе

Ответы: [`topics/aiohttp/aiohttp.md`](./topics/aiohttp/aiohttp.md)

### `rest-drf`

- APIView vs generic views (`ListCreateAPIView`)
- DRF
- forms Django vs DRF serializers
- parsers (JSON / MultiPart) — зачем
- REST, методы HTTP, коды ответов
- Serializer (DRF)
- throttling
- идемпотентность; PUT vs PATCH
- Пагинация, фильтрация, сортировка
- статус 400 vs 401 vs 403 vs 404

Ответы: [`topics/rest-drf/rest-drf.md`](./topics/rest-drf/rest-drf.md)

### `security`

- bleach
- CAPTCHA
- CORS
- middleware, CSRF
- SQL-инъекции — что это, почему ORM безопаснее raw SQL
- XSS, SQL injection

Ответы: [`topics/security/security.md`](./topics/security/security.md)

### `auth`

- JWT — auth без сессии
- permissions / authentication classes
- Аутентификация vs авторизация

Ответы: [`topics/auth/auth.md`](./topics/auth/auth.md)

### `caching`

- Cache — что кэшировать (список комментов), Redis cache
- redis
- Отличие: Redis как cache vs Redis как channel layer

Ответы: [`topics/caching/caching.md`](./topics/caching/caching.md)

### `queues`

- Celery «зачем»
- Queue — зачем очередь (фон: ресайз, письма, антиспам)

Ответы: [`topics/queues/queues.md`](./topics/queues/queues.md)

### `realtime`

- ASGI (Daphne) vs обычный runserver
- ASGI vs WSGI
- channels-redis
- Daphne
- Django Channels
- Events / pub-sub
- WebSocket
- WebSocket vs HTTP

Ответы: [`topics/realtime/realtime.md`](./topics/realtime/realtime.md)

### `frontend`

- fetch / FormData
- Vite
- Vue 3

Ответы: [`topics/frontend/frontend.md`](./topics/frontend/frontend.md)

### `docker-infra`

- Docker
- docker compose
- env-переменные / секреты
- image vs container vs volume
- Reverse proxy (nginx)
- логирование

Ответы: [`topics/docker-infra/docker-infra.md`](./topics/docker-infra/docker-infra.md)

### `git`

- .gitignore / не коммитить секреты
- branch / merge / rebase
- conflict
- Git

Ответы: [`topics/git/git.md`](./topics/git/git.md)

### `practices`

- SOLID, KISS, DRY, YAGNI
- Какие знаешь паттерны проектирования, какие использовал

Ответы: [`topics/practices/practices.md`](./topics/practices/practices.md)

### `ai-tools`

- Что такое AI-assisted development
- Cursor / Copilot / Claude Code — зачем
- Как писать полезный промпт к коду
- Когда ИИ врёт и как это ловить
- Что оставлять за человеком
- Как говорить об этом на собесе

Ответы: [`topics/ai-tools/ai-tools.md`](./topics/ai-tools/ai-tools.md)

### `english`

- Present Simple — + / − / ? for I, you/we/they, he/she/it
- Present Continuous — + / − / ?
- Past Simple / Continuous — + / − / ?
- Present Perfect / Perfect Continuous / Past Perfect
- Future: will / going to / Present Continuous
- Active vs Passive (+ − ? by tense)
- Conditionals 0–3
- Modals (can, must, should, might, would)
- Articles / countable / comparatives (short)
- Interview chunks + speaking prompts

Ответы: [`topics/english/english.md`](./topics/english/english.md)
