# Что такое context manager (`with`)? Зачем нужен?

## Коротко

Протокол гарантированного входа/выхода (`__enter__`/`__exit__`), чтобы ресурсы закрывались даже при ошибке. 

## Развёрнуто

`with open(path) as f` закроет файл. `with transaction.atomic()` откатит транзакцию при исключении. Можно писать свои через класс или `@contextmanager`.

## Пример

Код: [`context_manager_demo.py`](./examples/context_manager_demo.py)

```python
"""

Dependencies: none (stdlib)
context manager — гарантия очистки ресурса."""

class CM:
 def __enter__(self):
 print("open")
 return self

 def __exit__(self, exc_type, exc, tb):
 print("close")
 return False # не глотаем исключения

with CM():
 print("work")
```
