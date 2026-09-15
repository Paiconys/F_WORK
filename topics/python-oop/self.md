# Что такое self в классах?

## Коротко

Явная ссылка на конкретный экземпляр, с которым вызван метод. 

## Развёрнуто

При `obj.method(x)` Python вызывает `Class.method(obj, x)`. Имя `self` — соглашение. Через него читают/меняют состояние объекта. Без понимания `self` путают классовые и объектные атрибуты.

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
