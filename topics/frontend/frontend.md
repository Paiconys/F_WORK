# Frontend

Вопросы в этом блоке:

1. [fetch / FormData](#fetch--formdata)
2. [Vite](#vite)
3. [Vue 3](#vue-3)

---

### fetch / FormData

#### Коротко
Браузерный API для HTTP-запросов; `FormData` — удобная упаковка полей и файлов.

#### Развёрнуто
`fetch` возвращает Promise, сам JSON не парсит — нужен `response.json()`. Для файлов: `FormData` + `multipart/form-data` (boundary выставит браузер, `Content-Type` руками лучше не ломать). Ошибки: проверяй `response.ok`/статус, не только сеть. На собесе отличи от «полноценного» клиента (axios): interceptors, таймауты — вручную или библиотекой.

---

### Vite

#### Коротко
Dev-server и сборщик фронтенда (быстрый HMR, нативная работа с ESM).

#### Развёрнуто
В dev часто настраивают proxy на backend, чтобы ходить на один origin и не упираться в CORS. В prod — `build` статики (JS/CSS), которые отдаёт nginx или другой static server. Альтернативы: Webpack, Parcel. На собесе: Vite ≠ фреймворк UI; это tooling вокруг Vue/React/…

---

### Vue 3

#### Коротко
Фреймворк UI для реактивного интерфейса (компоненты, Composition/Options API).

#### Развёрнуто
Идея SPA: страница не перезагружается целиком, данные приходят с API (`fetch`/axios), UI обновляется реактивно. На собесе: компоненты, props/emits, lifecycle, зачем store (Pinia), отличие от серверного рендера Django Templates. Vue — не замена backend-валидации.

---
