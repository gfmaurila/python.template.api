import asyncio
from worker.User.RedisSubscriber import RedisSubscriber
from worker.User.RabbitSubscriber import RabbitMQSubscriber
from worker.User.KafkaSubscriber import KafkaSubscriber

async def start_all():
    print("Iniciando subscribers...")

    for canal in ["user-created", "user-deleted", "user-updated"]:
        asyncio.create_task(RedisSubscriber(channel=canal).listen())

    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, lambda: RabbitMQSubscriber().listen())
    loop.run_in_executor(None, lambda: KafkaSubscriber().listen())

    while True:
        await asyncio.sleep(3600)  # mantém o worker rodando

if __name__ == "__main__":
    asyncio.run(start_all())
