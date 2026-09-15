# FastAPI

Вопросы в этом блоке:

1. [Что такое FastAPI и зачем он](#что-такое-fastapi-и-зачем-он)
2. [ASGI и почему FastAPI быстрый](#asgi-и-почему-fastapi-быстрый)
3. [Path / Query параметры и type hints](#path--query-параметры-и-type-hints)
4. [Pydantic-модели для body](#pydantic-модели-для-body)
5. [Depends — что это](#depends--что-это)
6. [async def vs def в хендлерах](#async-def-vs-def-в-хендлерах)
7. [Автодокументация OpenAPI](#автодокументация-openapi)
8. [FastAPI vs Django/DRF — когда что](#fastapi-vs-djangodrf--когда-что)

---

### Что такое FastAPI и зачем он

#### Коротко
Современный Python-фреймворк для HTTP API на ASGI: быстрый старт, type hints, автовалидация и OpenAPI из коробки.

#### Развёрнуто
Идея: описал сигнатуры и Pydantic-модели — получил валидацию входа/выхода и `/docs`. Хорош для микросервисов и API-first. Не заменяет «батарейки» Django (admin, ORM, auth из коробки) — часто рядом SQLAlchemy/другое.

#### Пример
Код: [`hello_fastapi.py`](./examples/hello_fastapi.py)

```python
"""Минимальный FastAPI endpoint.

Dependencies:
  pip install fastapi uvicorn
Запуск:
  uvicorn hello_fastapi:app --reload
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health() -> dict:
    return {"ok": True}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None) -> dict:
    return {"item_id": item_id, "q": q}
```

---

### ASGI и почему FastAPI быстрый

#### Коротко
Работает поверх ASGI (часто Starlette + Uvicorn): async I/O, один процесс обслуживает много ожиданий сети.

#### Развёрнуто
Скорость — не «магия языка», а неблокирующие ожидания + тонкий стек. CPU-bound код всё равно упрётся в GIL; тяжёлое — в процессы/очередь. На собесе: ASGI vs WSGI, роль Uvicorn/Gunicorn+Uvicorn workers.

---

### Path / Query параметры и type hints

#### Коротко
`item_id: int` в path и `q: str | None` в query — FastAPI парсит и валидирует по аннотациям.

#### Развёрнуто
Неверные типы → 422 с понятным телом ошибки. `Query`/`Path` дают constraints (min/max, regex). Это контракт API без ручного `int(request.GET[...])`.

---

### Pydantic-модели для body

#### Коротко
Тело запроса описываешь классом BaseModel — получаешь парсинг JSON и ошибки валидации.

#### Развёрнуто
Модели = схема данных. `response_model` режет/проверяет ответ. Версии Pydantic v2 чуть отличаются API — на собесе достаточно идеи «схема + валидация».

---

### Depends — что это

#### Коротко
Механизм внедрения зависимостей: auth, сессия БД, общий клиент — без глобальных синглтонов в каждом хендлере.

#### Развёрнуто
`Depends(get_db)` вызывается фреймворком, умеет вложенность и override в тестах. Аналог «middleware + явная передача», но типобезопасно и тестируемо.

---

### async def vs def в хендлерах

#### Коротко
`async def` — для await I/O; обычный `def` FastAPI гоняет в threadpool, чтобы не блокировать loop.

#### Развёрнуто
Синхронный ORM/тяжёлый CPU в `async def` без `to_thread`/executor — антипаттерн. Правило: блокирующее → `def` или вынести; чистый async I/O → `async def`.

---

### Автодокументация OpenAPI

#### Коротко
`/docs` (Swagger) и `/redoc` строятся из кода: пути, схемы, коды.

#### Развёрнуто
Документация не «отдельный Confluence», а следствие аннотаций. На проде иногда закрывают `/docs` или защищают auth.

---

### FastAPI vs Django/DRF — когда что

#### Коротко
FastAPI — лёгкие/async API и микросервисы; Django/DRF — полный веб-продукт с админкой, ORM, экосистемой.

#### Развёрнуто
Выбор не «кто быстрее на бенчмарке», а scope: нужен admin/CMS/batteries → Django; нужен тонкий API рядом с ML/агентами → часто FastAPI. Оба умеют REST; паттерны валидации разные (Serializer vs Pydantic).
