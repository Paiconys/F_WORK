# bleach

## Коротко

Санитизация **HTML** — HyperText Markup Language (язык разметки) по белому списку тегов/атрибутов. 

## Развёрнуто

Главный инструмент закрытия XSS в тексте комментария по whitelist.

## Пример

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
