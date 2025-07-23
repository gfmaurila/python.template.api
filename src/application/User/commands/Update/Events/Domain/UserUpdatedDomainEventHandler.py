from datetime import timedelta
from domain.entities.User.events.UserUpdatedDomainEvent import UserUpdatedDomainEvent
from application.User.queries.GetAllUsersQuery import GetAllUsersQuery
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

        # Logger
        self._logger = logging.getLogger("UserUpdatedDomainEventHandler")

        # Repositório
        self._repository: IUserRepository = UserRepository()

        # Cache Redis
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

        # Chave principal da lista de usuários
        cacheKeyAll = "GetAllUsersQuery"
        await self._cacheService.DeleteAsync(cacheKeyAll)

        query = GetAllUsersQuery(self._repository)

        async def load_users():
            users = await query.Handle()
            return [UserQueryModel.from_entity(u).model_dump() for u in users]

        await self._cacheService.GetOrCreateAsync(
            cacheKeyAll,
            load_users,
            expiry=None  # ← cache sem expiração
        )

        # Chave individual
        cacheKeySingle = f"UserUpdated:{event.Id}"

        # Buscar usuário atualizado
        user = await self._repository.GetById(event.Id)
        if not user:
            self._logger.warning(f"[WARN] Usuário {event.Id} não encontrado para cache individual.")
            return

        userData = UserQueryModel.from_entity(user).model_dump()

        # Salvar registro individual no Redis (sem expiração)
        await self._cacheService.SetAsync(
            cacheKeySingle,
            userData,
            expiry=None
        )
