# src/application/User/events/UserCreatedDomainEventHandler.py

from datetime import timedelta
from domain.entities.User.events.UserCreatedDomainEvent import UserCreatedDomainEvent
from application.User.queries.GetAllUsersQuery import GetAllUsersQuery
from domain.interfaces.IUserRepository import IUserRepository
from core.domain.interfaces.IRedisCacheService import IRedisCacheService
from infrastructure.repositories.UserRepository import UserRepository
from infrastructure.service.RedisCacheService import RedisCacheService
from core.domain.model.CacheOptions import CacheOptions
from core.Config import GetSettings
from application.User.dtos.UserQueryModel import UserQueryModel

import logging


class UserCreatedDomainEventHandler:
    def __init__(self):
        settings = GetSettings()

        # Logger padrão
        self._logger = logging.getLogger("UserCreatedDomainEventHandler")

        # Repositório
        self._repository: IUserRepository = UserRepository()

        # Cache Redis com parâmetros completos
        cacheOptions = CacheOptions(
            DbIndex=settings.REDIS_DB,
            AbsoluteExpirationInHours=2,
            SlidingExpirationInSeconds=0
        )
        redisUrl = f"redis://:{settings.REDIS_PASSWORD}@{settings.REDIS_HOST}:{settings.REDIS_PORT}/{settings.REDIS_DB_USER}"

        self._cacheService: IRedisCacheService[list] = RedisCacheService(
            cacheOptions=cacheOptions,
            redisUrl=redisUrl
        )

    async def Handle(self, event: UserCreatedDomainEvent):
        cacheKey = "GetAllUsersQuery"

        self._logger.info(f"[EVENT] UserCreatedDomainEvent triggered for: {event.Name} ({event.Email})")

        # Limpa cache
        await self._cacheService.DeleteAsync(cacheKey)

        # Recria cache com a lista atualizada de usuários
        query = GetAllUsersQuery(self._repository)

        async def load_users():
            users = await query.Handle()
            return [UserQueryModel.from_entity(u).model_dump() for u in users]  # <- serializável
        
        # await self._cacheService.GetOrCreateAsync(
        #     cacheKey,
        #     load_users,
        #     expiry=timedelta(hours=2)
        # )

        await self._cacheService.GetOrCreateAsync(
            cacheKey,
            load_users,
            expiry=None  # <- cache eterno (ou até ser removido manualmente)
        )




