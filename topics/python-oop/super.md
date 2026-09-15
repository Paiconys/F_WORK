# Зачем нужен метод super в классе?

## Коротко

Чтобы вызвать следующий метод по **MRO** — Method Resolution Order (порядок разрешения методов) (обычно родителя) без жёсткого имени базового класса. 

## Развёрнуто

Критичен при множественном наследовании/миксинах: `super().__init__(...)` идёт правильно по цепочке. В Py3 пишут `super()`. Хардкод `Parent.method(self)` ломается при ромбах и рефакторинге.

## Пример

Код: [`super_demo.py`](./examples/super_demo.py)

```python
"""

Dependencies: none (stdlib)
super() идёт по MRO, не «всегда к прямому родителю по имени»."""

class A:
 def f(self):
 return "A"

class B(A):
 def f(self):
 return "B+" + super().f()

print(B().f()) # B+A
```
