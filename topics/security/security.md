# Безопасность веб

Вопросы в этом блоке:

1. [bleach](#bleach)
2. [CAPTCHA](#captcha)
3. [CORS](#cors)
4. [middleware, CSRF](#middleware-csrf)
5. [SQL-инъекции — что это, почему ORM безопаснее raw SQL](#sql-инъекции--что-это-почему-orm-безопаснее-raw-sql)
6. [XSS, SQL injection](#xss-sql-injection)

---

### bleach

#### Коротко
Санитизация **HTML** — HyperText Markup Language (язык разметки) по белому списку тегов/атрибутов. 

#### Развёрнуто
Главный инструмент закрытия XSS в тексте комментария по whitelist.

#### Пример
Код: [`bleach_demo.py`](./examples/bleach_demo.py)

```python
"""Whitelist HTML через bleach (XSS).

Dependencies:
  pip install bleach
"""

import re

import bleach

ALLOWED_TAGS = ["a", "code", "i", "strong"]
ALLOWED_ATTRS = {"a": ["href", "title"]}


def sanitize(html: str) -> str:
    # script/style вычищаем целиком (иначе strip оставит текст внутри)
    html = re.sub(r"<(script|style)\b[^>]*>[\s\S]*?</\1>", "", html, flags=re.I)
    return bleach.clean(
        html,
        tags=ALLOWED_TAGS,
        attributes=ALLOWED_ATTRS,
        strip=True,
    )


if __name__ == "__main__":
    dirty = '<b>nope</b><script>alert(1)</script><strong>ok</strong> <a href="https://x.test">x</a>'
    print(sanitize(dirty))
```

---

### CAPTCHA

#### Коротко
Проверка «запрос сделал человек», а не простой бот: одноразовый challenge, проверка на сервере.

#### Развёрнуто
Схема: сервер выдаёт ключ/картинку → клиент шлёт ответ → сервер сверяет и **инвалидирует** ключ. Клиентская «проверка» недостаточна. На API важно: не принимать POST без успешной серверной валидации. Варианты: классическая captcha, reCAPTCHA/hCaptcha, rate-limit + honeypot как дополнение.

---

### CORS

#### Коротко
**CORS** — Cross-Origin Resource Sharing (совместное использование ресурсов между источниками). Политика браузера: JS с одного origin не читает ответы другого без разрешения сервера.

#### Развёрнуто
Нужен, когда фронт и API на разных доменах/портах как разных origin. Сервер шлёт Access-Control-*. Часто один origin через proxy — CORS почти не болит, но вопрос любят задавать.

---

### middleware, CSRF

#### Коротко
Middleware — конвейер вокруг request/response; **CSRF** — Cross-Site Request Forgery (межсайтовая подделка запроса) мешает чужому сайту слать state-changing запросы от имени вашей cookie-сессии. 

#### Развёрнуто
Порядок middleware важен. CSRF токен сверяется на небезопасных методах при session-auth. Для чисто token/API картинка другая. У SPA за одним origin через proxy тема часто «тише», но смысл CSRF всё равно надо уметь объяснить.

---

### SQL-инъекции — что это, почему ORM безопаснее raw SQL

#### Коротко
**ORM** — Object-Relational Mapping (объектно-реляционное отображение). SQLi — поломка запроса входными данными; ORM по умолчанию параметризует значения. 

#### Развёрнуто
Опасно: `f"WHERE name='{user}'"`. Безопаснее: `.filter(name=user)`. Raw SQL допустим только осознанно с параметрами. Типичный акцент на безопасности API.

---

### XSS, SQL injection

#### Коротко
**XSS** — Cross-Site Scripting (межсайтовый скриптинг) — выполнение чужого скрипта в браузере жертвы; SQLi — выполнение чужого **SQL** — Structured Query Language (язык структурированных запросов) через ввод. 

#### Развёрнуто
XSS закрываем ограничением HTML (bleach whitelist) + корректным выводом; не доверяем «сырому» тексту. SQLi закрываем параметризованными запросами ORM, без склейки SQL строкой.

---
