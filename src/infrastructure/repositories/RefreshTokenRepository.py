import redis.asyncio as redis
from pymongo import MongoClient
from datetime import datetime, timedelta
from core.Config import GetSettings

class RefreshTokenRepository:
    def __init__(self):
        settings = GetSettings()

        self._redis = redis.from_url(
            f"redis://:{settings.REDIS_PASSWORD}@{settings.REDIS_HOST}:{settings.REDIS_PORT}/{settings.REDIS_DB_AUTH}"
        )

        mongo = MongoClient(settings.MONGO_LOG_CONN)
        self._collection = mongo[settings.MONGO_LOG_DB]["refresh_tokens"]

    async def Save(self, userId: str, refreshToken: str):
        key = f"refresh_token:{userId}"
        expires_in = 7 * 24 * 60 * 60

        await self._redis.set(key, refreshToken, ex=expires_in)

        self._collection.insert_one({
            "UserId": userId,
            "Token": refreshToken,
            "CreatedAt": datetime.utcnow(),
            "ExpiresAt": datetime.utcnow() + timedelta(seconds=expires_in)
        })
