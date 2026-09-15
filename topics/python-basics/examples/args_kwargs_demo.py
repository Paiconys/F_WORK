"""*args — кортеж, **kwargs — словарь.

Dependencies: none (stdlib)
"""


def f(a, *args, **kwargs):
    print("a=", a)
    print("args=", args)
    print("kwargs=", kwargs)


f(1, 2, 3, x=10, y=20)
