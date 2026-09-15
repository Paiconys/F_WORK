"""

Dependencies: none (stdlib)
lambda — короткое выражение, не полноценная функция."""

nums = [3, 1, 2]
print(sorted(nums, key=lambda x: x))
print(list(map(lambda x: x * 2, nums)))
