"""

Dependencies: none (stdlib)
dataclass — меньше шаблонного кода для данных."""

from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int = 0


print(User("Ada", 36))
