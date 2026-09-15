# Events / pub-sub

## Коротко

Издатель сообщает «что случилось», подписчики сами решают, как реагировать. 

## Развёрнуто

Обобщённый event bus vs наш практический случай: после create шлём событие в группу WS. Идея та же — слабая связанность производителя и потребителей.

## Пример

Код: [`channels_pubsub_demo.py`](./examples/channels_pubsub_demo.py)

```python
"""Идея pub/sub для realtime (stdlib), без Django Channels.

Channels в проде обычно: Redis channel layer + group_send.
Здесь — минимальная модель «событие -> подписчики».

Dependencies: none (stdlib)
"""

from collections import defaultdict

class Hub:
 def __init__(self) -> None:
 self._subs: dict[str, list] = defaultdict(list)

 def subscribe(self, group: str, handler) -> None:
 self._subs[group].append(handler)

 def publish(self, group: str, message: dict) -> None:
 for handler in self._subs.get(group, []):
 handler(message)

if __name__ == "__main__":
 hub = Hub()
 hub.subscribe("items", lambda m: print("client A", m))
 hub.subscribe("items", lambda m: print("client B", m))
 hub.publish("items", {"type": "created", "id": 7})
```
