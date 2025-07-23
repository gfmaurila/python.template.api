from datetime import timedelta
from domain.entities.User.events.UserDeletedDomainEvent import UserDeletedDomainEvent
from application.User.dtos.UserQueryModel import UserQueryModel
from domain.interfaces.IUserRepository import IUserRepository
from infrastructure.repositories.UserRepository import UserRepository
from core.domain.interfaces.IRedisCacheService import IRedisCacheService
from infrastructure.service.RedisCacheService import RedisCacheService
from core.domain.model.CacheOptions import CacheOptions
from core.Config import GetSettings

import logging


class UserDeletedDomainEventHandler:
    def __init__(self):
        settings = GetSettings()

        # Logger
        self._logger = logging.getLogger("UserDeletedDomainEventHandler")

        # Repositório
        self._repository: IUserRepository = UserRepository()

        # Cache Redis
        cacheOptions = CacheOptions(
            DbIndex=settings.REDIS_DB,
            AbsoluteExpirationInHours=24 * 365,  # 1 ano
            SlidingExpirationInSeconds=0
        )
        redisUrl = f"redis://:{settings.REDIS_PASSWORD}@{settings.REDIS_HOST}:{settings.REDIS_PORT}/{settings.REDIS_DB_USER_DELETE}"

        self._cacheService: IRedisCacheService[dict] = RedisCacheService(
            cacheOptions=cacheOptions,
            redisUrl=redisUrl
        )

    async def Handle(self, event: UserDeletedDomainEvent):
        cacheKey = f"UserDeleted:{event.Id}"

        self._logger.info(f"[EVENT] UserDeletedDomainEvent triggered for: {event.Name} ({event.Email})")

        # Buscar o usuário completo
        user = await self._repository.GetById(event.Id)
        if not user:
            self._logger.warning(f"[WARN] Usuário {event.Id} não encontrado no repositório.")
            return

        # Serializa para dicionário
        userData = UserQueryModel.from_entity(user).model_dump()

        # Salva no Redis por 1 ano
        await self._cacheService.SetAsync(
            cacheKey,
            userData,
            expiry=timedelta(days=365)
        )
