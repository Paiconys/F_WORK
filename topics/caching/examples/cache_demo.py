"""

Dependencies: none (stdlib)
Кэш: hit/miss и инвалидация (stdlib + опционально Redis).

Dependencies (optional Redis demo):
  pip install redis
  # и запущенный Redis на localhost:6379
"""

from functools import lru_cache
import time


@lru_cache(maxsize=128)
def expensive(x: int) -> int:
    time.sleep(0.05)
    return x * x


def demo_lru() -> None:
    t0 = time.perf_counter()
    print(expensive(10), expensive(10))  # второй вызов из кэша
    print("sec:", round(time.perf_counter() - t0, 3))
    expensive.cache_clear()  # инвалидация


def demo_redis() -> None:
    import redis  # dependency: redis

    r = redis.Redis(host="localhost", port=6379, decode_responses=True)
    key = "items:page:1"
    cached = r.get(key)
    if cached is None:
        value = '[{"id":1}]'  # будто дорогой SQL
        r.setex(key, 30, value)  # TTL 30s
        print("miss -> store", value)
    else:
        print("hit", cached)
    r.delete(key)  # invalidate on write


if __name__ == "__main__":
    demo_lru()
    # demo_redis()  # раскомментируй, если Redis доступен
