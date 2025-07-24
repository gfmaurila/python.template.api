# src/application/User/events/UserUpdatedDomainEventHandler.py

from domain.entities.User.events.UserUpdatedDomainEvent import UserUpdatedDomainEvent
from application.User.dtos.UserQueryModel import UserQueryModel
from domain.interfaces.IUserRepository import IUserRepository
from infrastructure.repositories.UserRepository import UserRepository
from core.domain.interfaces.IRedisCacheService import IRedisCacheService
from infrastructure.service.RedisCacheService import RedisCacheService
from core.domain.model.CacheOptions import CacheOptions
from core.Config import GetSettings

import logging

class UserUpdatedDomainEventHandler:
    def __init__(self):
        settings = GetSettings()

        self._logger = logging.getLogger("UserUpdatedDomainEventHandler")
        self._repository: IUserRepository = UserRepository()

        cacheOptions = CacheOptions(
            DbIndex=settings.REDIS_DB,
            AbsoluteExpirationInHours=0,
            SlidingExpirationInSeconds=0
        )
        redisUrl = f"redis://:{settings.REDIS_PASSWORD}@{settings.REDIS_HOST}:{settings.REDIS_PORT}/{settings.REDIS_DB_USER}"

        self._cacheService: IRedisCacheService[list | dict] = RedisCacheService(
            cacheOptions=cacheOptions,
            redisUrl=redisUrl
        )

    async def Handle(self, event: UserUpdatedDomainEvent):
        self._logger.info(f"[EVENT] UserUpdatedDomainEvent: {event.Name} ({event.Email})")

        # Atualiza lista completa no cache
        cacheKeyAll = "GetAllUsersQuery"
        await self._cacheService.DeleteAsync(cacheKeyAll)

        try:
            users = await self._repository.GetAll()
            serialized_users = [UserQueryModel.from_entity(u).model_dump() for u in users]
            await self._cacheService.SetAsync(cacheKeyAll, serialized_users)
        except Exception as ex:
            self._logger.error(f"[ERROR] Erro ao atualizar cache da lista: {ex}")
            return
