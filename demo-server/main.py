from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}


@app.get("/exec/{url}")
def read_exec():
    return


@app.get("/login/{trucs}")
def read_login():
    raise NotImplementedError()


@app.get("/signup/{trucs}")
def signup():
    raise NotImplementedError()


@app.get("/user")
def read_user():
    return


@app.get("/user/settings/{data}")
def settings(data: str):
    return {"data": data}
