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
