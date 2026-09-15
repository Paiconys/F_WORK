# Как в python реализуются методы объекта, класса и статические методы? Чем они отличаются?

## Коротко

Обычный метод получает экземпляр (`self`); `@classmethod` — класс (`cls`); `@staticmethod` — ничего из объекта/класса автоматически. 

## Развёрнуто

- **instance** — работа с данными объекта
- **classmethod** — фабрики/`from_json`, доступ к атрибутам класса 
- **staticmethod** — утилита в пространстве имён класса 
Отличие classmethod vs static: classmethod знает класс (важно при наследовании), static — просто функция.

## Пример

Код: [`methods_demo.py`](./examples/methods_demo.py)

```python
"""

Dependencies: none (stdlib)
instance / class / static methods."""

class A:
 def inst(self):
 return "instance", self

 @classmethod
 def cls(cls):
 return "class", cls

 @staticmethod
 def st():
 return "static"

print(A().inst()[0], A.cls()[0], A.st())
```
