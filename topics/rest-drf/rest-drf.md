# REST / DRF

Вопросы в этом блоке:

1. [APIView vs generic views (`ListCreateAPIView`)](#apiview-vs-generic-views-listcreateapiview)
2. [DRF](#drf)
3. [forms Django vs DRF serializers](#forms-django-vs-drf-serializers)
4. [parsers (JSON / MultiPart) — зачем](#parsers-json--multipart--зачем)
5. [REST, методы HTTP, коды ответов](#rest-методы-http-коды-ответов)
6. [Serializer (DRF)](#serializer-drf)
7. [throttling](#throttling)
8. [идемпотентность; PUT vs PATCH](#идемпотентность-put-vs-patch)
9. [Пагинация, фильтрация, сортировка](#пагинация-фильтрация-сортировка)
10. [статус 400 vs 401 vs 403 vs 404](#статус-400-vs-401-vs-403-vs-404)

---

### APIView vs generic views (`ListCreateAPIView`)

#### Коротко
APIView — полный контроль руками; generic views — готовые кубики **CRUD** — Create, Read, Update, Delete (создание, чтение, обновление, удаление). 

#### Развёрнуто
`ListCreateAPIView` закрыл list+create и хорошо лег на пагинацию/ordering. `CaptchaNewView` оставили простым APIView — там один GET без модели-коллекции.

---

### DRF

#### Коротко
**DRF** — Django REST Framework (REST-фреймворк для Django). Инструментарий REST поверх Django. 

#### Развёрнуто
Сериализаторы, generic views, pagination, parsers для multipart — меньше бойлерплейта и единый стиль ошибок.

---

### forms Django vs DRF serializers

#### Коротко
**ORM** — Object-Relational Mapping (объектно-реляционное отображение). Forms заточены под HTML-формы/admin; serializers — под API и JSON/multipart. 

#### Развёрнуто
Оба валидируют и чистят данные. В SPA UI-форма на фронте, серверная правда — Serializer; django.forms не обязателен.

---

### parsers (JSON / MultiPart) — зачем

#### Коротко
Парсеры объясняют **DRF** — Django **REST** — Representational State Transfer (архитектурный стиль API) Framework, как разобрать body разных Content-Type. 

#### Развёрнуто
JSON — обычные клиенты. Multipart — upload файла вместе с полями. Без MultiPartParser файл из формы не придёт нормально.

---

### REST, методы HTTP, коды ответов

#### Коротко
Ресурсы и стандартные HTTP-глаголы; успех/ошибки — статус-кодами.

#### Развёрнуто
Ресурс вроде `/api/items/`: GET — читать коллекцию, POST — создать. Не RPC вида `/createItem`. Коды: 2xx успех, 4xx ошибка клиента, 5xx сервер. Типично: 200 list, 201 create, 400 validation, 401/403 authz, 404 not found. Идемпотентность: повтор GET/PUT безопаснее по смыслу, чем повтор POST.

---

### Serializer (DRF)

#### Коротко
Граница API: принять данные, провалидировать, превратить в объект/ответ (и обратно).

#### Развёрнуто
Не «просто JSON». Ответственности: валидация полей, `validate`/`validate_<field>`, создание/обновление (`create`/`update`), представление вложенных связей, иногда side-effects (но тяжёлое лучше выносить). Модель хранит данные; serializer — контракт HTTP. Forms Django решают похожую задачу для HTML-форм.

---

### throttling

#### Коротко
Ограничение частоты запросов, чтобы не задолбить **API** — Application Programming Interface (программный интерфейс приложения). 

#### Развёрнуто
По IP/user, scoped на view. Полезно на captcha/create. Если не включено — хороший ответ «что бы добавил под нагрузкой».

---

### идемпотентность; PUT vs PATCH

#### Коротко
Идемпотентность — повтор запроса с тем же эффектом; PUT заменяет ресурс целиком, PATCH меняет частично. 

#### Развёрнуто
Повторный DELETE того же id — всё ещё «ресурса нет». POST обычно не идемпотентен (каждый раз может создать новое). В нашем API update нет — но отличие PUT/PATCH спрашивают часто.

---

### Пагинация, фильтрация, сортировка

#### Коротко
Пагинация режет выдачу страницами; фильтры сужают выборку; сортировка задаёт порядок.

#### Развёрнуто
Зачем: не отдавать всю таблицу, стабильный UX и меньше нагрузки. В DRF — pagination class, `OrderingFilter`, `FilterSet`/query params. Важно пагинировать «корень» списка осмысленно (например корни дерева, а не каждый узел как отдельную строку ленты). Всегда документируй дефолтный order (часто `-created_at`).

---

### статус 400 vs 401 vs 403 vs 404

#### Коротко
400 — невалидный запрос; 401 — не представился; 403 — представился, но нельзя; 404 — ресурса нет.

#### Развёрнуто
Путать 401/403 — частая ошибка. Неверная captcha — 400 (данные плохие), не 401. Нет page=999 с данными — часто пустой results/404 по политике пагинации.

---
