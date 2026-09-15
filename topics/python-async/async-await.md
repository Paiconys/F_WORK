# Что такое async и await?

## Коротко

`async def` объявляет корутину; `await` ждёт результат awaitable, не блокируя loop на ожидании **I/O** — Input/Output (ввод/вывод). 

## Развёрнуто

Вызов `async def` возвращает coroutine object — его нужно await/schedule. В синхронный Django view просто так не воткнуть. async в Channels consumer; мост в sync — `async_to_sync`.

## Пример

Код: [`async_demo.py`](./examples/async_demo.py)

```python
"""

Dependencies: none (stdlib)
Минимальная идея async/await (нужен event loop)."""

import asyncio

async def fetch(name):
 await asyncio.sleep(0.01) # «ждём I/O», не блокируя loop
 return name

async def main():
 a, b = await asyncio.gather(fetch("A"), fetch("B"))
 print(a, b)

if __name__ == "__main__":
 asyncio.run(main())
```
