# Что такое GIL, какие проблемы он решает, плюсы и минусы

## Коротко

**GIL** — Global Interpreter Lock (глобальная блокировка интерпретатора). В CPython глобальная блокировка: один поток исполняет bytecode — упрощает память, мешает CPU-параллелизму в threads. 

## Развёрнуто

Плюс: проще модель объектов/refcount. Минус: CPU-bound на threads не масштабируется. На I/O GIL часто отпускается — веб живёт. Обходы: multiprocessing, async I/O, нативные расширения, другой интерпретатор (редко тема Junior).

## Пример

Код: [`concurrency_demo.py`](./examples/concurrency_demo.py)

```python
"""Threads / processes / asyncio — когда что.

Dependencies: none (stdlib)
"""

# I/O-bound -> threading или asyncio
# CPU-bound -> multiprocessing (GIL мешает потокам на чистом Python CPU)
# много сетевых ожиданий в одном процессе -> asyncio

print("pick model by bottleneck: I/O -> threads/asyncio, CPU -> processes")
```
