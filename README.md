# F_WORK — теория к техсобесу

Только **что это / зачем / как работает** + примеры кода.
Без soft-skills и без вырезок из конкретного проекта.

## Структура

```
topics/<тема>/
  README.md
  <вопрос>.md      # Коротко → Развёрнуто → Пример
  examples/*.py
```

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-examples.txt

python topics/drills/examples/mro_super_abc.py
```

## Темы

- [`python-types`](./topics/python-types/) — Python — типы, мутабельность, сравнение (4)
- [`python-functions`](./topics/python-functions/) — Python — функции и выражения (5)
- [`python-oop`](./topics/python-oop/) — Python — ООП, MRO, декораторы (13)
- [`python-iterators`](./topics/python-iterators/) — Python — итераторы и генераторы (3)
- [`python-async`](./topics/python-async/) — Python — async, GIL, параллелизм (7)
- [`python-testing`](./topics/python-testing/) — Python — тестирование (4)
- [`python-packaging`](./topics/python-packaging/) — Python — окружение, модули, импорты (5)
- [`python-stdlib`](./topics/python-stdlib/) — Python — исключения, with, dataclass (4)
- [`python-complexity`](./topics/python-complexity/) — Python — сложность алгоритмов (2)
- [`databases`](./topics/databases/) — Базы данных (14)
- [`orm`](./topics/orm/) — ORM (4)
- [`django`](./topics/django/) — Django (16)
- [`rest-drf`](./topics/rest-drf/) — REST / DRF (10)
- [`security`](./topics/security/) — Безопасность веб (6)
- [`auth`](./topics/auth/) — Аутентификация и авторизация (3)
- [`caching`](./topics/caching/) — Кэш (3)
- [`queues`](./topics/queues/) — Очереди и фоновые задачи (2)
- [`realtime`](./topics/realtime/) — Realtime: WebSocket, Channels, events (8)
- [`frontend`](./topics/frontend/) — Frontend (Vue) (3)
- [`docker-infra`](./topics/docker-infra/) — Docker и инфраструктура (6)
- [`git`](./topics/git/) — Git (4)
- [`practices`](./topics/practices/) — Практики (SOLID, паттерны) (2)
- [`drills`](./topics/drills/) — Тренажёр: угадай вывод (4)

## Не кладём сюда

- soft («как рассказать про опыт», команда, дедлайны)
- кейсы конкретного ТЗ/проекта (LIFO 25, homepage, lightbox…)
- карточки «как у нас в compose»

## Правила

1. Карточка = теория для техсобеса.
2. Пример либо stdlib, либо с `Dependencies:` в `.py`.

## Git

Чтобы Cursor не попадал в `Co-authored-by` коммитов:

```bash
git config core.hooksPath .githooks
```
