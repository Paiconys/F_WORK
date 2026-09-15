# Что такое генератор? Как написать на Python генератор?

## Коротко

Ленивый итератор, который пишут функцией с `yield` или generator expression. 

## Развёрнуто

`def gen(): yield 1; yield 2` — при вызове сразу не считается. Память экономится на больших потоках. `(x*x for x in xs)` — genexp. Генератор — частный случай итератора.

## Пример

Код: [`iter_gen_demo.py`](./examples/iter_gen_demo.py)

```python
"""

Dependencies: none (stdlib)
Итератор vs генератор."""

def gen():
 yield 1
 yield 2

g = gen()
print(next(g), next(g))

# generator expression — лениво
squares = (x * x for x in range(5))
print(list(squares))
```
