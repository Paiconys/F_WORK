"""

Dependencies: none (stdlib)
Простой декоратор и декоратор с аргументами."""

from functools import wraps


def simple(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("before")
        result = fn(*args, **kwargs)
        print("after")
        return result

    return wrapper


def repeat(n):
    def deco(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                fn(*args, **kwargs)

        return wrapper

    return deco


@simple
def hello():
    print("hi")


@repeat(2)
def ping():
    print("pong")


if __name__ == "__main__":
    hello()
    ping()
