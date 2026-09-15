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
