import asyncio
from fastapi import FastAPI
from contextlib import asynccontextmanager

from api import MessagingTestController, UserController
from core.Openapi import CustomOpenapi
from infrastructure.messaging.User.Sub.RedisSubscriber import RedisSubscriber
from infrastructure.messaging.User.Sub.RabbitSubscriber import RabbitMQSubscriber

from infrastructure.messaging.User.Sub.KafkaSubscriber import start_kafka_subscriber

from core.Config import GetSettings
settings = GetSettings()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    for canal in ["user-created", "user-deleted", "user-updated"]:
        subscriber = RedisSubscriber(channel=canal)
        asyncio.create_task(subscriber.listen())
        print(f"RedisSubscriber iniciado em background. - {canal}")

    asyncio.get_event_loop().run_in_executor(
        None,
        lambda: RabbitMQSubscriber().listen()
    )
    print("RabbitMQSubscriber iniciado em background.")

    # Kafka Subscriber
    asyncio.get_event_loop().run_in_executor(
        None,
        lambda: start_kafka_subscriber()
    )
    print("KafkaSubscriber iniciado em background.")

    yield

    # Optional shutdown logic aqui (se necessário)

app = FastAPI(lifespan=lifespan)
app.openapi = lambda: CustomOpenapi(app)

@app.get("/")
def read_root():
    return {"message": "API Python Template com DDD, CQRS e Vertical Slices"}

app.include_router(UserController.router)
app.include_router(MessagingTestController.router)
