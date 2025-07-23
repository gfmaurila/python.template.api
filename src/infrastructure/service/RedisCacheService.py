# src/infrastructure/service/RedisCacheService.py

import json
import redis.asyncio as redis
from typing import Optional, Callable, List, TypeVar, Generic, Awaitable
from datetime import timedelta

from core.domain.model.CacheOptions import CacheOptions
from core.domain.interfaces.IRedisCacheService import IRedisCacheService

T = TypeVar("T")


class RedisCacheService(IRedisCacheService[T], Generic[T]):
    def __init__(self, cacheOptions: CacheOptions, redisUrl: str):
        self.CacheOptions = cacheOptions
        self.RedisUrl = redisUrl
        self.Redis = None

    async def _GetRedis(self):
        if self.Redis is None:
            self.Redis = redis.from_url(
                self.RedisUrl,
                db=self.CacheOptions.DbIndex,
                decode_responses=True
            )
        return self.Redis

    async def SetAsync(self, key: str, value: T, expiry: Optional[timedelta] = None) -> bool:
        redisConn = await self._GetRedis()
        expireSeconds = int(expiry.total_seconds()) if expiry else None
        valueStr = json.dumps(value)
        return await redisConn.set(key, valueStr, ex=expireSeconds)

    async def AddToListAsync(self, listKey: str, value: T) -> int:
        redisConn = await self._GetRedis()
        valueStr = json.dumps(value)
        return await redisConn.rpush(listKey, valueStr)

    async def GetOrCreateAsync(self, key: str, createItem: Callable[[], Awaitable[T]], expiry: Optional[timedelta] = None) -> T:
        redisConn = await self._GetRedis()
        valueStr = await redisConn.get(key)
        if valueStr:
            return json.loads(valueStr)

        item = await createItem()  # <- await corretamente o retorno da função async
        await self.SetAsync(key, item, expiry)
        return item

    async def GetListAsync(self, listKey: str) -> List[T]:
        redisConn = await self._GetRedis()
        values = await redisConn.lrange(listKey, 0, -1)
        return [json.loads(item) for item in values if item]

    async def RemoveFromListAsync(self, listKey: str, value: T) -> int:
        redisConn = await self._GetRedis()
        valueStr = json.dumps(value)
        return await redisConn.lrem(listKey, 0, valueStr)

    async def GetAsync(self, key: str) -> Optional[T]:
        redisConn = await self._GetRedis()
        valueStr = await redisConn.get(key)
        return json.loads(valueStr) if valueStr else None

    async def DeleteAsync(self, key: str) -> bool:
        redisConn = await self._GetRedis()
        return await redisConn.delete(key) > 0

    async def ClearDatabaseAsync(self) -> None:
        redisConn = await self._GetRedis()
        await redisConn.flushdb()

