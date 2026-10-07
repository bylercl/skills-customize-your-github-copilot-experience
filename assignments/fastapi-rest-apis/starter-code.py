from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Simple API")


class Item(BaseModel):
    title: str
    done: bool = False


items = [
    {"id": 1, "title": "Learn FastAPI", "done": True},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}


# TODO: Add GET /items and POST /items endpoints
# TODO: Validate input with the Item model
# TODO: Return created items with IDs
