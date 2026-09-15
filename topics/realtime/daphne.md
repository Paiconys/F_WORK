# Daphne

## Коротко

ASGI-сервер (часто рядом с Django Channels).

## Развёрнуто

WSGI-сервер (gunicorn/uwsgi в классике) не обслуживает WebSocket. Daphne принимает HTTP и WS по ASGI. Альтернативы: Uvicorn, Hypercorn. На собесе: «для Channels нужен ASGI-сервер, не runserver как прод-цель».
