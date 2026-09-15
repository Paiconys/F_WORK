# HttpRequest / HttpResponse

## Коротко

Request — входящее сообщение клиента; Response — то, что сервер возвращает. 

## Развёрнуто

У request есть method, path, headers, body, user. Response — status + body + headers. DRF оборачивает их удобнее (`Request`/`Response`), но идея та же.
