# APIView vs generic views (`ListCreateAPIView`)

## Коротко

APIView — полный контроль руками; generic views — готовые кубики **CRUD** — Create, Read, Update, Delete (создание, чтение, обновление, удаление). 

## Развёрнуто

`ListCreateAPIView` закрыл list+create и хорошо лег на пагинацию/ordering. `CaptchaNewView` оставили простым APIView — там один GET без модели-коллекции.
