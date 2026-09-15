# fetch / FormData

## Коротко

Браузерный API для HTTP-запросов; `FormData` — удобная упаковка полей и файлов.

## Развёрнуто

`fetch` возвращает Promise, сам JSON не парсит — нужен `response.json()`. Для файлов: `FormData` + `multipart/form-data` (boundary выставит браузер, `Content-Type` руками лучше не ломать). Ошибки: проверяй `response.ok`/статус, не только сеть. На собесе отличи от «полноценного» клиента (axios): interceptors, таймауты — вручную или библиотекой.
