# aiohttp

Вопросы в этом блоке:

1. [Что такое aiohttp](#что-такое-aiohttp)
2. [Client vs Server API](#client-vs-server-api)
3. [Application, Router, Request/Response](#application-router-requestresponse)
4. [Зачем ClientSession](#зачем-clientsession)
5. [aiohttp vs FastAPI / asyncio](#aiohttp-vs-fastapi--asyncio)
6. [Типичные ошибки на собесе](#типичные-ошибки-на-собесе)

---

### Что такое aiohttp

#### Коротко
Библиотека для **async** HTTP: и клиент, и сервер на asyncio.

#### Развёрнуто
Ниже уровнем, чем FastAPI: сам собираешь routing, middlewares, сериализацию. Гибко для микросервисов и высоконагруженного I/O. Часто рядом с чистым asyncio без «магических» фреймворков.

#### Пример
Код: [`hello_aiohttp.py`](./examples/hello_aiohttp.py)

```python
"""Минимальный aiohttp server.

Dependencies:
  pip install aiohttp
Запуск:
  python hello_aiohttp.py
"""

from aiohttp import web


async def health(request: web.Request) -> web.Response:
    return web.json_response({"ok": True})


def main() -> None:
    app = web.Application()
    app.router.add_get("/health", health)
    web.run_app(app, host="127.0.0.1", port=8080)


if __name__ == "__main__":
    main()
```

---

### Client vs Server API

#### Коротко
Один пакет — два режима: `ClientSession` ходит наружу; `web.Application` принимает запросы.

#### Развёрнуто
На собесе уточняй контекст: «писали сервис» vs «ходили в чужой API». Путать client/server — частая ошибка.

---

### Application, Router, Request/Response

#### Коротко
`Application` держит роуты и состояние; хендлер получает `Request`, возвращает `Response`/`json_response`.

#### Развёрнуто
Middlewares — обёртки вокруг хендлеров. Состояние (пул БД) кладут в `app` на startup и закрывают на cleanup. Это ручной lifecycle vs Depends в FastAPI.

---

### Зачем ClientSession

#### Коротко
Переиспользует соединения (connection pool); не создавай session на каждый запрос в цикле.

#### Развёрнуто
`async with ClientSession() as session:` на время задачи/приложения. Таймауты, headers, connector limits — настраиваются на session. Утечки session → «too many open files».

---

### aiohttp vs FastAPI / asyncio

#### Коротко
asyncio — event loop; aiohttp — HTTP на asyncio; FastAPI — высокоуровневый API-фреймворк (часто над Starlette), не замена aiohttp 1:1.

#### Развёрнуто
Вакансии с «aiohttp обязательно» ждут опыт именно этого стека (роутинг, session, async handlers), не только «знаю async/await». FastAPI удобнее для OpenAPI/Pydantic; aiohttp — контроль и legacy/highload сервисы.

---

### Типичные ошибки на собесе

#### Коротко
Блокирующий код в async-хендлере; новая ClientSession на каждый request; забытый await; путаница client/server.

#### Развёрнуто
Проговаривай: где await, где executor для sync ORM, как тестировать (`aiohttp.test_utils`). Связь с Celery: тяжёлое/долгий CPU не в request path.
