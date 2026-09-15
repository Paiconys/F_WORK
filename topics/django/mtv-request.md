# MTV / что происходит с request

## Коротко

Request проходит middleware → URL → view → (модель/БД) → response; MTV = Model–Template–View (в API вместо template — JSON/serializer). 

## Развёрнуто

Daphne принимает HTTP. Middleware (security/session/csrf/auth…). `urls.py` выбирает view. View часто на DRF: serializer + ORM. Model — данные. Template в классике рендерит HTML; В SPA HTML рисует фронт, Django/DRF отдаёт данные. Цепочка «что происходит с request» важнее зубрить аббревиатуру.
