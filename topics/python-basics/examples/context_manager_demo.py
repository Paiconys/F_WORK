"""context manager — гарантия очистки ресурса.

Dependencies: none (stdlib)
"""


class CM:
    def __enter__(self):
        print("open")
        return self

    def __exit__(self, exc_type, exc, tb):
        print("close")
        return False  # не глотаем исключения


with CM():
    print("work")
