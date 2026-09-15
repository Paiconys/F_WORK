# threading vs multiprocessing vs asyncio (когда что)

## Коротко

Threads — **I/O** — Input/Output (ввод/вывод); processes — **CPU** — Central Processing Unit (процессор); asyncio — много сетевых ожиданий в одном потоке.

## Развёрнуто

Если упираетесь в расчёт — процессы/нативный код. Если ждёте диск/сеть пачками — threads или async. Если десятки тысяч соединений — async/ASGI. Веб+WS ближе к async-серверу; тяжёлый фон — очередь.

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
