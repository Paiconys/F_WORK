# settings: DEBUG, SECRET_KEY, ALLOWED_HOSTS

## Коротко

DEBUG включает отладку; SECRET_KEY — секрет для подписей; ALLOWED_HOSTS — белый список Host. 

## Развёрнуто

В проде DEBUG=False (иначе traceback и лишние дыры). SECRET_KEY только из env, не из git. ALLOWED_HOSTS = домен/IP, с которых ждёте запросы. Неправильный Host → DisallowedHost.
