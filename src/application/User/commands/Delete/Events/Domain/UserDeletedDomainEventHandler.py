from datetime import timedelta
from domain.entities.User.events.UserDeletedDomainEvent import UserDeletedDomainEvent
from application.User.dtos.UserQueryModel import UserQueryModel
from application.User.services.UserCacheRefresher import UserCacheRefresher
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

        self._logger = logging.getLogger("UserDeletedDomainEventHandler")
        self._repository: IUserRepository = UserRepository()

        # Cache individual para usuário deletado
        cacheOptions = CacheOptions(
            DbIndex=settings.REDIS_DB,
            AbsoluteExpirationInHours=24 * 365,
            SlidingExpirationInSeconds=0
        )
        redisUrlDeleted = f"redis://:{settings.REDIS_PASSWORD}@{settings.REDIS_HOST}:{settings.REDIS_PORT}/{settings.REDIS_DB_USER_DELETE}"
        self._cacheService: IRedisCacheService[dict] = RedisCacheService(
            cacheOptions=cacheOptions,
            redisUrl=redisUrlDeleted
        )

    async def Handle(self, event: UserDeletedDomainEvent):
        cacheKey = f"UserDeleted:{event.Id}"

        self._logger.info(f"[EVENT] UserDeletedDomainEvent triggered for: {event.Name} ({event.Email})")

        # Buscar o usuário completo
        user = await self._repository.GetById(event.Id)
        if not user:
            self._logger.warning(f"[WARN] Usuário {event.Id} não encontrado no repositório.")
            return

        # Salvar usuário deletado no Redis por 1 ano
        userData = UserQueryModel.from_entity(user).model_dump()
        await self._cacheService.SetAsync(cacheKey, userData, expiry=timedelta(days=365))
        self._logger.info(f"[CACHE] Usuário deletado armazenado com chave: {cacheKey}")

        # Atualiza a lista GetAllUsersQuery com a lógica compartilhada
        # Debito tecnico
        # Fazer uma publicação na fila para que isso posso ser executando mais tarde
        refresher = UserCacheRefresher()
        await refresher.RefreshGetAllUsersQuery()
