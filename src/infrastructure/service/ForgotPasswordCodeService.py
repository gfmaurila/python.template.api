import redis.asyncio as redis
import uuid
from core.Config import GetSettings

class ForgotPasswordCodeService:
    def __init__(self):
        settings = GetSettings()
        self._redis = redis.from_url(
            f"redis://:{settings.REDIS_PASSWORD}@{settings.REDIS_HOST}:{settings.REDIS_PORT}/{settings.REDIS_DB_USER}"
        )

    async def GenerateCode(self, userId: int) -> str:
        code = str(uuid.uuid4())
        await self._redis.set(f"reset_code:{code}", userId, ex=900)
        return code

    async def GetUserIdByCode(self, code: str) -> int | None:
        result = await self._redis.get(f"reset_code:{code}")
        return int(result) if result else None

    async def DeleteCode(self, code: str):
        await self._redis.delete(f"reset_code:{code}")