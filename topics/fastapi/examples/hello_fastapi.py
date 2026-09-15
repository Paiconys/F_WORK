"""Минимальный FastAPI endpoint.

Dependencies:
  pip install fastapi uvicorn
Запуск:
  uvicorn hello_fastapi:app --reload
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health() -> dict:
    return {"ok": True}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None) -> dict:
    return {"item_id": item_id, "q": q}
