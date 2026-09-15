"""Минимальная идея async/await (нужен event loop).

Dependencies: none (stdlib)
"""

import asyncio


async def fetch(name):
    await asyncio.sleep(0.01)  # «ждём I/O», не блокируя loop
    return name


async def main():
    a, b = await asyncio.gather(fetch("A"), fetch("B"))
    print(a, b)


if __name__ == "__main__":
    asyncio.run(main())
