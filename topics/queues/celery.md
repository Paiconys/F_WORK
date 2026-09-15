# Celery «зачем»

## Коротко

Чтобы долгие задачи не держать внутри **HTTP** — Hypertext Transfer Protocol (протокол передачи гипертекста)-воркера пользователя.

## Развёрнуто

Письма, ресайз пачек, отчёты, ретраи. Брокер + воркеры. Если ресайз делать синхронно в POST — под нагрузкой начнёте таймаутить. пока в request path — честный gap .

## Пример

Код: [`queue_demo.py`](./examples/queue_demo.py)

```python
"""

Dependencies: none (stdlib)
Очередь задач: HTTP не ждёт тяжёлую работу.

Вариант A (stdlib) — всегда работает.
Вариант B (Celery) — нужен брокер.

Dependencies for Celery variant:
 pip install celery redis
 # redis-server + celery -A queue_demo worker -l info
"""

from __future__ import annotations

import queue
import threading
import time

def stdlib_worker(q: queue.Queue) -> None:
 while True:
 job = q.get()
 if job is None:
 q.task_done()
 break
 name, payload = job
 print("worker got", name, payload)
 time.sleep(0.05)
 q.task_done()

def demo_stdlib() -> None:
 q: queue.Queue = queue.Queue()
 t = threading.Thread(target=stdlib_worker, args=(q,), daemon=True)
 t.start()
 q.put(("resize", {"file": "a.jpg"}))
 q.put(("email", {"to": "a@b.c"}))
 q.put(None)
 q.join()
 print("request thread finished without waiting for heavy work inline")

# --- Celery (optional) ---
try:
 from celery import Celery

 app = Celery("demo", broker="redis://localhost:6379/0")

 @app.task
 def resize(path: str) -> str:
 return f"resized:{path}"

except ImportError:
 app = None
 resize = None

if __name__ == "__main__":
 demo_stdlib()
 # if app and resize:
 # resize.delay("photo.jpg")
```
