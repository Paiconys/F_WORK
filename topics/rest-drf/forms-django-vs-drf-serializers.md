# forms Django vs DRF serializers

## Коротко

**ORM** — Object-Relational Mapping (объектно-реляционное отображение). Forms заточены под HTML-формы/admin; serializers — под API и JSON/multipart. 

## Развёрнуто

Оба валидируют и чистят данные. В SPA UI-форма на фронте, серверная правда — Serializer; django.forms не обязателен.
