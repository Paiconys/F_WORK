"""== сравнивает значение, is — идентичность объекта.

Dependencies: none (stdlib)
"""

a = [1, 2]
b = [1, 2]
c = a

print(a == b)  # True  — одинаковое содержимое
print(a is b)  # False — разные объекты
print(a is c)  # True  — тот же объект
