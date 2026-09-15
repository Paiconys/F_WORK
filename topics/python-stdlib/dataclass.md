# dataclass — что это, зачем

## Коротко

Декоратор, который сам собирает шаблонный код для класса-данных (`__init__`, сравнение и т.д.). 

## Развёрнуто

Удобно для DTO/конфигов без тяжёлой логики. Не замена моделям ORM. Есть `frozen`, `slots` и т.п.

## Пример

Код: [`dataclass_demo.py`](./examples/dataclass_demo.py)

```python
"""

Dependencies: none (stdlib)
dataclass — меньше шаблонного кода для данных."""

from dataclasses import dataclass

@dataclass
class User:
 name: str
 age: int = 0

print(User("Ada", 36))
```
