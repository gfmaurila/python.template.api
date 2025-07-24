# src/application/User/queries/GetAllUsersQuery.py

from domain.interfaces.IUserRepository import IUserRepository
from core.domain.interfaces.IRedisCacheService import IRedisCacheService
from application.User.dtos.UserQueryModel import UserQueryModel

from core.domain.model.CacheOptions import CacheOptions
from infrastructure.service.RedisCacheService import RedisCacheService
from core.Config import GetSettings

from datetime import timedelta

class GetAllUsersQuery:
    def __init__(self, repository: IUserRepository):
        self._repository = repository

        # Configurar Redis
        settings = GetSettings()
        redisUrl = f"redis://:{settings.REDIS_PASSWORD}@{settings.REDIS_HOST}:{settings.REDIS_PORT}/{settings.REDIS_DB_USER}"
        cacheOptions = CacheOptions(
            DbIndex=settings.REDIS_DB,
            AbsoluteExpirationInHours=1,  # pode ajustar
            SlidingExpirationInSeconds=0
        )
        self._cacheService: IRedisCacheService[list] = RedisCacheService(
            cacheOptions=cacheOptions,
            redisUrl=redisUrl
        )

    async def Handle(self):
        cacheKey = "GetAllUsersQuery"

        async def load_from_db():
            users = await self._repository.GetAll()
            return [UserQueryModel.from_entity(u).model_dump() for u in users]

        return await self._cacheService.GetOrCreateAsync(
            cacheKey,
            load_from_db,
            expiry=timedelta(hours=1)
        )
