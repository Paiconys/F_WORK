"""Минимальный aiohttp server.

Dependencies:
  pip install aiohttp
Запуск:
  python hello_aiohttp.py
"""

from aiohttp import web


async def health(request: web.Request) -> web.Response:
    return web.json_response({"ok": True})


def main() -> None:
    app = web.Application()
    app.router.add_get("/health", health)
    web.run_app(app, host="127.0.0.1", port=8080)


if __name__ == "__main__":
    main()
