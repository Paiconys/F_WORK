# permissions / authentication classes

## Коротко

Authentication наполняет `request.user`; permissions решают, пустить ли к view. 

## Развёрнуто

Можно отключить на публичных эндпоинтах. Связка с JWT: authentication достаёт пользователя из токена, permission говорит `IsAuthenticated`/`IsAdminUser`.
