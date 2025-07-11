# main.py

import asyncio
from fastapi import FastAPI

from api import UserController
from core.Openapi import CustomOpenapi
from infrastructure.messaging.RedisSubscriber import RedisSubscriber

app = FastAPI()
app.openapi = lambda: CustomOpenapi(app)

@app.get("/")
def read_root():
    return {"message": "API Python Template com DDD, CQRS e Vertical Slices"}

app.include_router(UserController.router)

@app.on_event("startup")
async def startup_event():
    subscriber = RedisSubscriber(channel="user-created")
    asyncio.create_task(subscriber.listen())
    print("RedisSubscriber iniciado em background.")
