from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from routers.auth import router as AuthRouter

app = FastAPI()

app.include_router(AuthRouter)


@app.get("/")
def read_info():
    return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: str, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


# @app.put("/items/{item_id}")
# def update_item(item_id: str, item: Item):
#     return {"item_id": item_id, "item_name": item.name, "item_price": item.price, "item_is_offer": item.is_offer}
