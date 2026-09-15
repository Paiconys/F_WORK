# ForeignKey, on_delete, related_name

## Коротко

**FK** — Foreign Key (внешний ключ) — ссылка на другую строку; `on_delete` задаёт судьбу детей при удалении родителя; `related_name` — имя обратной связи. 

## Развёрнуто

`parent = ForeignKey('self', related_name='replies', on_delete=CASCADE)` даёт дерево и `comment.replies`. Без `related_name` было бы `comment_set`. `on_delete` — не «опция красоты», а правило целостности.
