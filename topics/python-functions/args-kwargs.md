# Что такое args и kwargs? Чем представлены?

## Коротко

`*args` — кортеж лишних позиционных аргументов, `**kwargs` — словарь лишних именованных. 

## Развёрнуто

Нужны для обёрток, декораторов, проброса в `super().__init__(*args, **kwargs)`. Имена условные, синтаксис `*`/`**` обязателен. При вызове `f(*args, **kwargs)` наоборот распаковывают.

## Пример

Код: [`args_kwargs_demo.py`](./examples/args_kwargs_demo.py)

```python
"""

Dependencies: none (stdlib)
*args — кортеж, **kwargs — словарь."""

def f(a, *args, **kwargs):
 print("a=", a)
 print("args=", args)
 print("kwargs=", kwargs)

f(1, 2, 3, x=10, y=20)
```
