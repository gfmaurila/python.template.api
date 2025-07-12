import redis
import json
from core.Config import GetSettings

settings = GetSettings()

class RedisPublisher:
    def __init__(self):
        self.client = redis.Redis(
            host=settings.REDIS_HOST,         
            port=settings.REDIS_PORT,
            db=settings.REDIS_DB,
            password=settings.REDIS_PASSWORD,
            decode_responses=True
        )

    def publish(self, channel: str, message: dict):
        payload = json.dumps(message)
        self.client.publish(channel, payload)
        print(f"[REDIS] Publicado em '{channel}': {payload}")
