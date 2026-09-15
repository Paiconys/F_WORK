# что такое lambda функция. кейсы применения

## Коротко

Однострочная анонимная функция из одного выражения — для коротких callback’ов. 

## Развёрнуто

`lambda x: x[1]` как `key` в `sorted`, редко в `map`/`filter`. Если нужны условия, несколько строк, имя для трейсбека — обычный `def`. Lambda не место для бизнес-логики.

## Пример

Код: [`lambda_demo.py`](./examples/lambda_demo.py)

```python
"""

Dependencies: none (stdlib)
lambda — короткое выражение, не полноценная функция."""

nums = [3, 1, 2]
print(sorted(nums, key=lambda x: x))
print(list(map(lambda x: x * 2, nums)))
```
