# list comprehension / generator expression — отличия

## Коротко

Comprehension сразу строит list в памяти; genexp лениво отдаёт элементы. 

## Развёрнуто

`[x for x in xs if ...]` vs `(x for x in xs if ...)`. Для больших потоков genexp/генератор безопаснее по RAM. Для маленьких коллекций list comp читаемее и нормален.
