# Vite

## Коротко

Dev-server и сборщик фронтенда (быстрый HMR, нативная работа с ESM).

## Развёрнуто

В dev часто настраивают proxy на backend, чтобы ходить на один origin и не упираться в CORS. В prod — `build` статики (JS/CSS), которые отдаёт nginx или другой static server. Альтернативы: Webpack, Parcel. На собесе: Vite ≠ фреймворк UI; это tooling вокруг Vue/React/…
