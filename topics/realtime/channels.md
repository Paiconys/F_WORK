# Django Channels

## Коротко

Расширение Django для протоколов помимо HTTP: в первую очередь WebSocket.

## Развёрнуто

Добавляет ASGI-приложение, routing и consumers (обработчики соединений). Для нескольких воркеров нужен channel layer (часто Redis), иначе group_send живёт только в памяти одного процесса. На собесе отличи от «просто asyncio»: Channels встраивает realtime в экосистему Django (auth, ORM через sync_to_async/async_to_sync).
