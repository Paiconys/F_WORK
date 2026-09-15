# middleware, CSRF

## Коротко

Middleware — конвейер вокруг request/response; **CSRF** — Cross-Site Request Forgery (межсайтовая подделка запроса) мешает чужому сайту слать state-changing запросы от имени вашей cookie-сессии. 

## Развёрнуто

Порядок middleware важен. CSRF токен сверяется на небезопасных методах при session-auth. Для чисто token/API картинка другая. У SPA за одним origin через proxy тема часто «тише», но смысл CSRF всё равно надо уметь объяснить.
