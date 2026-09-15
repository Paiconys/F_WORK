# JOIN / что делает ORM вместо JOIN

## Коротко

**ORM** — Object-Relational Mapping (объектно-реляционное отображение). JOIN в SQL склеивает строки таблиц по условию; ORM прячет это в `select_related`/`prefetch_related` и связях моделей. 

## Развёрнуто

`select_related` для FK/OneToOne делает JOIN/связанный запрос заранее. `prefetch_related` для reverse/M2M — обычно отдельный запрос + склейка в Python. Цель та же, что у JOIN: не ходить в БД N раз.
