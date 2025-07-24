# src/application/User/events/UserCreatedDomainEventHandler.py

from domain.entities.User.events.UserCreatedDomainEvent import UserCreatedDomainEvent
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

        self._logger = logging.getLogger("UserCreatedDomainEventHandler")
        self._repository: IUserRepository = UserRepository()
        
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

        try:
            
            # Atualiza lista completa no cache
            await self._cacheService.DeleteAsync(cacheKey)

            # Busca todos os usuários atualizados do banco
            users = await self._repository.GetAll()

            # Transforma todos em modelos serializáveis
            serialized_users = [UserQueryModel.from_entity(u).model_dump() for u in users]

            # Atualiza o cache com a lista completa
            await self._cacheService.SetAsync(cacheKey, serialized_users)

        except Exception as ex:
            self._logger.error(f"[ERROR] Falha ao atualizar o cache: {ex}")
