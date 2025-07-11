import asyncio
import redis
from core.Config import GetSettings

settings = GetSettings()

class RedisSubscriber:
    def __init__(self, channel: str):
        self.channel = channel
        self.client = redis.Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            db=settings.REDIS_DB,
            password=settings.REDIS_PASSWORD,
            decode_responses=True
        )

    async def listen(self):
        pubsub = self.client.pubsub()
        pubsub.subscribe(self.channel)

        print(f"Subscrito no canal Redis: {self.channel}")
        while True:
            message = pubsub.get_message(ignore_subscribe_messages=True, timeout=1.0)
            if message:
                print(f"[REDIS - {self.channel}] Mensagem recebida:", message["data"])
            await asyncio.sleep(0.01)
