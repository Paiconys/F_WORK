# MRO + super().bar() — D(B, C) где B(A)

## Коротко

Печатает `A`: MRO D→B→A→C, B без bar, A с bar.

## Развёрнуто

До C очередь не доходит. C3/MRO — не «первый родитель в скобках», а линейный порядок.

## Пример

Код: [`mro_super_ba.py`](./examples/mro_super_ba.py)

```python
"""

Dependencies: none (stdlib)
DRILL: другой граф наследования — ответ уже не B."""

class A:
 def bar(self):
 print("A")

class B(A):
 def foo(self):
 print("B")

class C:
 def bar(self):
 print("C")

class D(B, C):
 def bar(self):
 super().bar()

obj = D()
obj.bar() # -> A

print(D.__mro__)
# (D, B, A, C, object) — B без bar, A с bar; до C не доходим
```
