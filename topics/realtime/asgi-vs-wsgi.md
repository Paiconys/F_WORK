# ASGI vs WSGI

## Коротко

**WSGI** — Web Server Gateway Interface (интерфейс шлюза веб-сервера) — синхронный контракт для HTTP; **ASGI** — Asynchronous Server Gateway Interface (асинхронный интерфейс сервера) — async и WebSocket. 

## Развёрнуто

Классический gunicorn+WSGI не закроет WS из коробки. Daphne/Uvicorn+ASGI — наш путь из-за Channels. Для «просто JSON API» хватило бы WSGI; для live — ASGI.
