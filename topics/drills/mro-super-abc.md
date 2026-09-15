# MRO + super().bar() — D(A, B, C)

## Коротко

Печатает `B`: MRO идёт D→A→B→C, у A нет bar, у B есть.

## Развёрнуто

Всегда проговаривай `Class.__mro__`, потом ищи первый класс с нужным методом после текущего.

## Пример

Код: [`mro_super_abc.py`](./examples/mro_super_abc.py)

```python
"""

Dependencies: none (stdlib)
DRILL: какой метод вызовет super().bar()?

MRO: всегда смотри Class.__mro__
"""

class A:
 def foo(self):
 print("A")

class B:
 def bar(self):
 print("B")

class C:
 def bar(self):
 print("C")

class D(A, B, C):
 def bar(self):
 # super() = следующий класс в MRO после D
 super().bar()

obj = D()
obj.bar() # -> B

print(D.__mro__)
# (D, A, B, C, object) — у A нет bar, у B есть
```
