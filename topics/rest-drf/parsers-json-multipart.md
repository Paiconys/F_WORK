# parsers (JSON / MultiPart) — зачем

## Коротко

Парсеры объясняют **DRF** — Django **REST** — Representational State Transfer (архитектурный стиль API) Framework, как разобрать body разных Content-Type. 

## Развёрнуто

JSON — обычные клиенты. Multipart — upload файла вместе с полями. Без MultiPartParser файл из формы не придёт нормально.
