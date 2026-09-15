# `get_queryset` vs атрибут `queryset`

## Коротко

Атрибут — фиксированный queryset; метод — когда набор зависит от логики/request. 

## Развёрнуто

Мы в `get_queryset` всегда режем `parent__isnull=True` и вешаем prefetch. Так нельзя «случайно» отдать все replies как корни.
