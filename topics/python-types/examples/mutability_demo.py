"""

Dependencies: none (stdlib)
Mutable vs immutable и передача в функцию."""


def rebind(x):
    x = [99]  # локальная перепривязка — снаружи не видно
    return x


def mutate(x):
    x.append(99)  # мутация объекта — видно снаружи


a = [1]
rebind(a)
print(a)  # [1]

mutate(a)
print(a)  # [1, 99]
