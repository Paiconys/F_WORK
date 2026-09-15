# Python — async / GIL / параллелизм

Вопросы в этом блоке:

1. [Asynchronous programming](#asynchronous-programming)
2. [Flask / Tornado](#flask--tornado)
3. [threading vs multiprocessing vs asyncio (когда что)](#threading-vs-multiprocessing-vs-asyncio-когда-что)
4. [Какие есть типы асинхронного выполнения?](#какие-есть-типы-асинхронного-выполнения)
5. [Что такое async и await?](#что-такое-async-и-await)
6. [Что такое GIL, какие проблемы он решает, плюсы и минусы](#что-такое-gil-какие-проблемы-он-решает-плюсы-и-минусы)
7. [Что такое корутина?](#что-такое-корутина)

---

### Asynchronous programming

#### Коротко
Умение писать конкурентный **I/O** — Input/Output (ввод/вывод) (async/await, **ASGI** — Asynchronous Server Gateway Interface (асинхронный интерфейс сервера)), не блокируя воркер на каждом ожидании. 

#### Развёрнуто
Channels consumer + ASGI-сервер — практический кусок async в вебе.

---

### Flask / Tornado

#### Коротко
Flask — минималистичный **WSGI** — Web Server Gateway Interface (интерфейс шлюза веб-сервера)-фреймворк; Tornado — свой async networking stack; Django — полный batteries-included. 

#### Развёрнуто
Flask гибок, но многое подключаешь сам. Tornado исторически для long-lived connections. Сегодня для API чаще FastAPI/Django; знание отличий важнее боевого опыта со всеми сразу.

---

### threading vs multiprocessing vs asyncio (когда что)

#### Коротко
Threads — **I/O** — Input/Output (ввод/вывод); processes — **CPU** — Central Processing Unit (процессор); asyncio — много сетевых ожиданий в одном потоке.

#### Развёрнуто
Если упираетесь в расчёт — процессы/нативный код. Если ждёте диск/сеть пачками — threads или async. Если десятки тысяч соединений — async/ASGI. Веб+WS ближе к async-серверу; тяжёлый фон — очередь.

#### Пример
Код: [`concurrency_demo.py`](./examples/concurrency_demo.py)

```python
"""Threads / processes / asyncio — когда что.

Dependencies: none (stdlib)
"""

# I/O-bound  -> threading или asyncio
# CPU-bound  -> multiprocessing (GIL мешает потокам на чистом Python CPU)
# много сетевых ожиданий в одном процессе -> asyncio

print("pick model by bottleneck: I/O -> threads/asyncio, CPU -> processes")
```

---

### Какие есть типы асинхронного выполнения?

#### Коротко
Потоки, процессы, кооперативный async (asyncio), плюс фоновые воркеры-очереди. 

#### Развёрнуто
- **threading** — I/O, упирается в GIL на CPU
- **multiprocessing** — CPU-bound, дороже по памяти 
- **asyncio** — много соединений в одном потоке 
- **task queue (Celery)** — работа вне веб-процесса 
Выбор зависит от того, ждёте ли вы сеть или считаете.

---

### Что такое async и await?

#### Коротко
`async def` объявляет корутину; `await` ждёт результат awaitable, не блокируя loop на ожидании **I/O** — Input/Output (ввод/вывод). 

#### Развёрнуто
Вызов `async def` возвращает coroutine object — его нужно await/schedule. В синхронный Django view просто так не воткнуть. async в Channels consumer; мост в sync — `async_to_sync`.

#### Пример
Код: [`async_demo.py`](./examples/async_demo.py)

```python
"""

Dependencies: none (stdlib)
Минимальная идея async/await (нужен event loop)."""

import asyncio


async def fetch(name):
    await asyncio.sleep(0.01)  # «ждём I/O», не блокируя loop
    return name


async def main():
    a, b = await asyncio.gather(fetch("A"), fetch("B"))
    print(a, b)


if __name__ == "__main__":
    asyncio.run(main())
```

---

### Что такое GIL, какие проблемы он решает, плюсы и минусы

#### Коротко
**GIL** — Global Interpreter Lock (глобальная блокировка интерпретатора). В CPython глобальная блокировка: один поток исполняет bytecode — упрощает память, мешает CPU-параллелизму в threads. 

#### Развёрнуто
Плюс: проще модель объектов/refcount. Минус: CPU-bound на threads не масштабируется. На I/O GIL часто отпускается — веб живёт. Обходы: multiprocessing, async I/O, нативные расширения, другой интерпретатор (редко тема Junior).

#### Пример
Код: [`concurrency_demo.py`](./examples/concurrency_demo.py)

```python
"""Threads / processes / asyncio — когда что.

Dependencies: none (stdlib)
"""

# I/O-bound  -> threading или asyncio
# CPU-bound  -> multiprocessing (GIL мешает потокам на чистом Python CPU)
# много сетевых ожиданий в одном процессе -> asyncio

print("pick model by bottleneck: I/O -> threads/asyncio, CPU -> processes")
```

---

### Что такое корутина?

#### Коротко
Подпрограмма, которую можно приостановить и продолжить; в современном Python — `async def`. 

#### Развёрнуто
Исторически были generator-based coroutine. Сейчас awaitable от `async def` крутит event loop. Нужны для конкурентного I/O. Не путать с потоками ОС.

#### Пример
Код: [`async_demo.py`](./examples/async_demo.py)

```python
"""

Dependencies: none (stdlib)
Минимальная идея async/await (нужен event loop)."""

import asyncio


async def fetch(name):
    await asyncio.sleep(0.01)  # «ждём I/O», не блокируя loop
    return name


async def main():
    a, b = await asyncio.gather(fetch("A"), fetch("B"))
    print(a, b)


if __name__ == "__main__":
    asyncio.run(main())
```

---
