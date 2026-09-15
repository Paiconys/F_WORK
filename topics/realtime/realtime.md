# Realtime: WebSocket / Channels

Вопросы в этом блоке:

1. [ASGI (Daphne) vs обычный runserver](#asgi-daphne-vs-обычный-runserver)
2. [ASGI vs WSGI](#asgi-vs-wsgi)
3. [channels-redis](#channels-redis)
4. [Daphne](#daphne)
5. [Django Channels](#django-channels)
6. [Events / pub-sub](#events--pub-sub)
7. [WebSocket](#websocket)
8. [WebSocket vs HTTP](#websocket-vs-http)

---

### ASGI (Daphne) vs обычный runserver

#### Коротко
runserver — удобный sync-dev для **HTTP** — Hypertext Transfer Protocol (протокол передачи гипертекста); Daphne — **ASGI** — Asynchronous Server Gateway Interface (асинхронный интерфейс сервера) и нужен для WebSocket. 

#### Развёрнуто
Для WebSocket обычный runserver недостаточен; нужен ASGI-сервер (например Daphne).

---

### ASGI vs WSGI

#### Коротко
**WSGI** — Web Server Gateway Interface (интерфейс шлюза веб-сервера) — синхронный контракт для HTTP; **ASGI** — Asynchronous Server Gateway Interface (асинхронный интерфейс сервера) — async и WebSocket. 

#### Развёрнуто
Классический gunicorn+WSGI не закроет WS из коробки. Daphne/Uvicorn+ASGI — наш путь из-за Channels. Для «просто JSON API» хватило бы WSGI; для live — ASGI.

---

### channels-redis

#### Коротко
Backend channel layer для Django Channels на Redis.

#### Развёрнуто
Channel layer — шина сообщений между consumer’ами/процессами (`group_add`, `group_send`). Redis-backend нужен, когда процессов больше одного (Docker, несколько workers). Это не то же самое, что Django cache: один Redis-сервер может играть разные роли.

---

### Daphne

#### Коротко
ASGI-сервер (часто рядом с Django Channels).

#### Развёрнуто
WSGI-сервер (gunicorn/uwsgi в классике) не обслуживает WebSocket. Daphne принимает HTTP и WS по ASGI. Альтернативы: Uvicorn, Hypercorn. На собесе: «для Channels нужен ASGI-сервер, не runserver как прод-цель».

---

### Django Channels

#### Коротко
Расширение Django для протоколов помимо HTTP: в первую очередь WebSocket.

#### Развёрнуто
Добавляет ASGI-приложение, routing и consumers (обработчики соединений). Для нескольких воркеров нужен channel layer (часто Redis), иначе group_send живёт только в памяти одного процесса. На собесе отличи от «просто asyncio»: Channels встраивает realtime в экосистему Django (auth, ORM через sync_to_async/async_to_sync).

---

### Events / pub-sub

#### Коротко
Издатель сообщает «что случилось», подписчики сами решают, как реагировать. 

#### Развёрнуто
Обобщённый event bus vs наш практический случай: после create шлём событие в группу WS. Идея та же — слабая связанность производителя и потребителей.

#### Пример
Код: [`channels_pubsub_demo.py`](./examples/channels_pubsub_demo.py)

```python
"""Идея pub/sub для realtime (stdlib), без Django Channels.

Channels в проде обычно: Redis channel layer + group_send.
Здесь — минимальная модель «событие -> подписчики».

Dependencies: none (stdlib)
"""

from collections import defaultdict


class Hub:
    def __init__(self) -> None:
        self._subs: dict[str, list] = defaultdict(list)

    def subscribe(self, group: str, handler) -> None:
        self._subs[group].append(handler)

    def publish(self, group: str, message: dict) -> None:
        for handler in self._subs.get(group, []):
            handler(message)


if __name__ == "__main__":
    hub = Hub()
    hub.subscribe("items", lambda m: print("client A", m))
    hub.subscribe("items", lambda m: print("client B", m))
    hub.publish("items", {"type": "created", "id": 7})
```

---

### WebSocket

#### Коротко
Канал live-уведомлений о новых комментариях.

#### Развёрнуто
Типичная связка: Channels + Redis layer + WS-клиент на фронте.

---

### WebSocket vs HTTP

#### Коротко
**HTTP** — Hypertext Transfer Protocol (протокол передачи гипертекста) — короткий запрос/ответ; WebSocket — долгоживущий двусторонний канал. 

#### Развёрнуто
HTTP идеален для CRUD. WS — когда сервер сам пушит «появился комментарий». Обычно не заменяем REST сокетом: REST пишет, WS сигналит обновить.

---
