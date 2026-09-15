# Django

Вопросы в этом блоке:

1. [`get_queryset` vs атрибут `queryset`](#get_queryset-vs-атрибут-queryset)
2. [admin — зачем](#admin--зачем)
3. [blank vs null](#blank-vs-null)
4. [Django + Django ORM](#django--django-orm)
5. [ForeignKey, on_delete, related_name](#foreignkey-on_delete-related_name)
6. [HttpRequest / HttpResponse](#httprequest--httpresponse)
7. [management commands (`migrate`, `shell`)](#management-commands-migrate-shell)
8. [MTV / что происходит с request](#mtv--что-происходит-с-request)
9. [N+1, select_related / prefetch_related](#n1-select_related--prefetch_related)
10. [Pillow](#pillow)
11. [settings: DEBUG, SECRET_KEY, ALLOWED_HOSTS](#settings-debug-secret_key-allowed_hosts)
12. [signals (хотя бы «что это»)](#signals-хотя-бы-что-это)
13. [static vs media](#static-vs-media)
14. [urlpatterns / path](#urlpatterns--path)
15. [миграции](#миграции)
16. [Миграции на проде](#миграции-на-проде)

---

### `get_queryset` vs атрибут `queryset`

#### Коротко
Атрибут — фиксированный queryset; метод — когда набор зависит от логики/request. 

#### Развёрнуто
В `get_queryset` удобно фильтровать и вешать `prefetch`/`select_related` в зависимости от request. Атрибут `queryset` — когда набор фиксированный.

---

### admin — зачем

#### Коротко
Встроенный **CRUD** — Create, Read, Update, Delete (создание, чтение, обновление, удаление) для моделей — быстрый взгляд на данные без фронта.

#### Развёрнуто
Удобно отлаживать дерево/вложения. Это инструмент разработчика/оператора, не замена публичному UI.

---

### blank vs null

#### Коротко
`blank` — про валидацию «можно пусто»; `null` — про NULL в колонке БД. 

#### Развёрнуто
Для строк Django обычно хранит `''` и ставит `blank=True` без `null=True`. Для FK/дат `null=True` осмысленнее. Путать их — классическая ошибка моделей. Необязательные строковые поля часто делают через `blank=True`.

---

### Django + Django ORM

#### Коротко
**ORM** — Object-Relational Mapping (объектно-реляционное отображение). Фреймворк приложения и встроенный способ говорить с таблицами через модели. 

#### Развёрнуто
Закрыли apps/settings/migrations/admin и запросы списка/создания без ручного SQL на каждый шаг.

---

### ForeignKey, on_delete, related_name

#### Коротко
**FK** — Foreign Key (внешний ключ) — ссылка на другую строку; `on_delete` задаёт судьбу детей при удалении родителя; `related_name` — имя обратной связи. 

#### Развёрнуто
`parent = ForeignKey('self', related_name='replies', on_delete=CASCADE)` даёт дерево и `comment.replies`. Без `related_name` было бы `comment_set`. `on_delete` — не «опция красоты», а правило целостности.

---

### HttpRequest / HttpResponse

#### Коротко
Request — входящее сообщение клиента; Response — то, что сервер возвращает. 

#### Развёрнуто
У request есть method, path, headers, body, user. Response — status + body + headers. DRF оборачивает их удобнее (`Request`/`Response`), но идея та же.

---

### management commands (`migrate`, `shell`)

#### Коротко
**CLI** — Command Line Interface (интерфейс командной строки) Django для служебных операций с проектом и данными. 

#### Развёрнуто
`migrate` — схема; `shell` — REPL с моделями; свои команды — для разовых job/скриптов. В проде осторожно с destructive-командами.

---

### MTV / что происходит с request

#### Коротко
Request проходит middleware → URL → view → (модель/БД) → response; MTV = Model–Template–View (в API вместо template — JSON/serializer). 

#### Развёрнуто
Daphne принимает HTTP. Middleware (security/session/csrf/auth…). `urls.py` выбирает view. View часто на DRF: serializer + ORM. Model — данные. Template в классике рендерит HTML; В SPA HTML рисует фронт, Django/DRF отдаёт данные. Цепочка «что происходит с request» важнее зубрить аббревиатуру.

---

### N+1, select_related / prefetch_related

#### Коротко
N+1 — один запрос списка и ещё по запросу на каждую связанную сущность; лечится предзагрузкой связей. 

#### Развёрнуто
Симптом: открыли 25 комментариев — и ещё 25+ запросов за replies/файлами. `select_related` — для FK/OneToOne (часто JOIN). `prefetch_related` — для обратных связей/M2M (отдельный запрос + сборка). prefetch в `get_queryset` списка корней.

#### Пример
Код: [`n_plus_one_demo.py`](./examples/n_plus_one_demo.py)

```python
"""N+1 vs select_related (Django ORM).

Dependencies:
  pip install Django
"""

import os
import django
from django.conf import settings
from django.db import connection, models


if not settings.configured:
    settings.configure(
        DEBUG=True,
        SECRET_KEY="dev",
        INSTALLED_APPS=["__main__"],
        DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}},
        USE_TZ=False,
    )
    django.setup()


class Author(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        app_label = "demo"


class Comment(models.Model):
    body = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        app_label = "demo"


def setup() -> None:
    with connection.schema_editor() as se:
        se.create_model(Author)
        se.create_model(Comment)
    a = Author.objects.create(name="Ada")
    Comment.objects.create(body="hi", author=a)
    Comment.objects.create(body="yo", author=a)


def bad() -> int:
    connection.queries_log.clear()
    for c in Comment.objects.all():
        _ = c.author.name  # N+1
    return len(connection.queries)


def good() -> int:
    connection.queries_log.clear()
    for c in Comment.objects.select_related("author"):
        _ = c.author.name
    return len(connection.queries)


if __name__ == "__main__":
    setup()
    print("queries bad:", bad())
    print("queries good:", good())
```

---

### Pillow

#### Коротко
Библиотека обработки изображений для Python (форк/наследник PIL).

#### Развёрнуто
На собесе: зачем — ресайз/конвертация/валидация загрузок на сервере, чтобы не хранить огромные оригиналы и не доверять клиенту. Типичный кейс: открыл файл → проверил тип → уменьшил до лимита → сохранил. Альтернативы: ImageMagick через CLI, облачные пайплайны, браузерный resize (но сервер всё равно должен проверять).

---

### settings: DEBUG, SECRET_KEY, ALLOWED_HOSTS

#### Коротко
DEBUG включает отладку; SECRET_KEY — секрет для подписей; ALLOWED_HOSTS — белый список Host. 

#### Развёрнуто
В проде DEBUG=False (иначе traceback и лишние дыры). SECRET_KEY только из env, не из git. ALLOWED_HOSTS = домен/IP, с которых ждёте запросы. Неправильный Host → DisallowedHost.

---

### signals (хотя бы «что это»)

#### Коротко
Сигналы — колбэки на события фреймворка/моделей (например `post_save`).

#### Развёрнуто
Позволяют реагировать без правки всех мест создания объекта. Риск — неявный поток «магии». Обычно для WS сознательно шлём событие из `create()`, а не из signal — проще трассировать.

---

### static vs media

#### Коротко
static — файлы приложения (css/js); media — пользовательские загрузки. 

#### Развёрнуто
Разные настройки и жизненный цикл. Static версионируются с релизом; media растут в volume и бэкапятся отдельно. Вложения комментариев — media.

---

### urlpatterns / path

#### Коротко
Маршрутизация HTTP: URL → view.

#### Развёрнуто
В `urls.py` список `path(...)` / `re_path(...)`, часто `include()` для приложений. Префиксы (`/api/`) задают границу API. 404 чаще из неверного include/префикса, чем из «сломанного» view. `name=` нужен для `reverse()`.

---

### миграции

#### Коротко
Версии схемы БД в коде: создаёшь файлы изменений и применяешь их на базу. 

#### Развёрнуто
`makemigrations` сравнивает модели и делает migration-файлы; `migrate` исполняет SQL-шаги. Это позволяет поднять пустую БД до актуального состояния. Часто migrate запускают на старте контейнера.

---

### Миграции на проде

#### Коротко
Менять схему БД версионированно, совместимо со старым кодом и с минимальным даунтаймом.

#### Развёрнуто
Риски: долгие ALTER/лок таблицы, несовместимость «новый код + старая схема» или наоборот. Приёмы: expand/contract (сначала добавить колонку nullable → задеплоить код → бэкфилл → NOT NULL), бэкап, прогон migrate в релизе, избегать разрушительных операций без плана отката. На собесе это про дисциплину поставки, не про `makemigrations` локально.

---
