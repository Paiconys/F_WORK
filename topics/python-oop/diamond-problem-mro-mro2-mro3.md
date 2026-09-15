# Что такое diamond problem? Что такое MRO? Чем отличается MRO2 от MRO3? Зачем оно нужно?

## Коротко

Ромб — два пути к одному предку; MRO — линейный порядок поиска методов; в Python 3 используют C3 (часто называют new-style/MRO «3»). 

## Развёрнуто

Без чёткого порядка непонятно, чей метод вызвать и куда пойдёт `super()`. Python строит `__mro__` алгоритмом C3; если линеаризовать нельзя — ошибка при создании класса. «MRO2 vs MRO3» на собесе обычно про старый classic-classes vs новый C3 в Py3: на практике смотри `__mro__` и доверяй `super()`. Зачем нужно — предсказуемое множественное наследование.

## Пример

Код: [`mro_demo.py`](./examples/mro_demo.py)

```python
"""

Dependencies: none (stdlib)
MRO / diamond — учебный пример к теории."""

class A:
 def f(self):
 return "A"

class B(A):
 def f(self):
 return "B+" + super().f()

class C(A):
 def f(self):
 return "C+" + super().f()

class D(B, C):
 pass

print(D().f()) # B+C+A (C3)
print(D.__mro__)
```
