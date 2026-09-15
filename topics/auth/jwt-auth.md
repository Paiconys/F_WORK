# JWT — auth без сессии

## Коротко

**JWT** — JSON Web Token (JSON-веб-токен). Клиент предъявляет подписанный токен вместо серверной session-cookie. 

## Развёрнуто

Stateless API удобно горизонтально масштабировать. Обычно access+refresh. Нужны privileges и logout/rotation-политика. В анонимном API логина может не быть — тогда JWT не нужен.

## Пример

Код: [`jwt_demo.py`](./examples/jwt_demo.py)

```python
"""JWT: encode / decode claims.

Dependencies:
  pip install PyJWT
"""

import datetime as dt

import jwt  # PyJWT

SECRET = "dev-only-secret-key-32-bytes-ok!!"  # HS256 wants >= 32 bytes
ALG = "HS256"


def make_access(user_id: int, minutes: int = 15) -> str:
    payload = {
        "sub": str(user_id),
        "typ": "access",
        "exp": dt.datetime.now(dt.timezone.utc) + dt.timedelta(minutes=minutes),
    }
    return jwt.encode(payload, SECRET, algorithm=ALG)


def read_access(token: str) -> dict:
    return jwt.decode(token, SECRET, algorithms=[ALG])


if __name__ == "__main__":
    token = make_access(42)
    print("token:", token)
    print("claims:", read_access(token))
```
