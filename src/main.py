from typing import Union
from fastapi import FastAPI
from routers.auth import router as AuthRouter

app = FastAPI()

app.include_router(AuthRouter)


@app.get("/")
def read_info():
    return {"Hello": "World"}
