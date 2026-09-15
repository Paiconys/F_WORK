# ASGI (Daphne) vs обычный runserver

## Коротко

runserver — удобный sync-dev для **HTTP** — Hypertext Transfer Protocol (протокол передачи гипертекста); Daphne — **ASGI** — Asynchronous Server Gateway Interface (асинхронный интерфейс сервера) и нужен для WebSocket. 

## Развёрнуто

Для WebSocket обычный runserver недостаточен; нужен ASGI-сервер (например Daphne).
