"""dataclass — меньше шаблонного кода для данных.

Dependencies: none (stdlib)
"""

from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int = 0


print(User("Ada", 36))
