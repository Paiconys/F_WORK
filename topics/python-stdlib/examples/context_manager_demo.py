"""

Dependencies: none (stdlib)
context manager — гарантия очистки ресурса."""


class CM:
    def __enter__(self):
        print("open")
        return self

    def __exit__(self, exc_type, exc, tb):
        print("close")
        return False  # не глотаем исключения


with CM():
    print("work")
