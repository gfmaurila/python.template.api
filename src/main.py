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

    # Inicia os dois subscribers
    created_subscriber = RedisSubscriber(channel="user-created")
    asyncio.create_task(created_subscriber.listen())
    print("RedisSubscribers iniciados em background. - user-created")
    
    deleted_subscriber = RedisSubscriber(channel="user-deleted")
    asyncio.create_task(deleted_subscriber.listen())
    print("RedisSubscribers iniciados em background. - user-deleted")

    updated_subscriber = RedisSubscriber(channel="user-updated")
    asyncio.create_task(updated_subscriber.listen())
    print("RedisSubscribers iniciados em background. - user-updated")
    
