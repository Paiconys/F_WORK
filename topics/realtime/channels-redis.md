# channels-redis

## Коротко

Backend channel layer для Django Channels на Redis.

## Развёрнуто

Channel layer — шина сообщений между consumer’ами/процессами (`group_add`, `group_send`). Redis-backend нужен, когда процессов больше одного (Docker, несколько workers). Это не то же самое, что Django cache: один Redis-сервер может играть разные роли.
