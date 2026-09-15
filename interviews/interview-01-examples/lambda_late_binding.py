"""DRILL: late binding — lambda в цикле.

Dependencies: none (stdlib)
"""

flist = []

for i in range(3):
    # Захватывается ИМЯ i, не значение на итерации
    flist.append(lambda: print(i))

[f() for f in flist]  # 2 2 2


# Фикс: дефолт фиксирует значение
flist2 = []
for i in range(3):
    flist2.append(lambda i=i: print(i))

[f() for f in flist2]  # 0 1 2
