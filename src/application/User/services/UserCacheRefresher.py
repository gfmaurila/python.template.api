# src/application/User/services/UserCacheRefresher.py

from application.User.dtos.UserQueryModel import UserQueryModel
from domain.interfaces.IUserRepository import IUserRepository
from infrastructure.repositories.UserRepository import UserRepository
from core.domain.interfaces.IRedisCacheService import IRedisCacheService
from infrastructure.service.RedisCacheService import RedisCacheService
from core.domain.model.CacheOptions import CacheOptions
from core.Config import GetSettings
import logging


class UserCacheRefresher:
    _executing = False  # proteção contra chamadas simultâneas

    def __init__(self):
        settings = GetSettings()
        self._logger = logging.getLogger("UserCacheRefresher")

        # Repositório puro, sem gerar eventos
        self._repository: IUserRepository = UserRepository()

        # Configuração de cache
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

    async def RefreshGetAllUsersQuery(self):
        if UserCacheRefresher._executing:
            self._logger.warning("[UserCacheRefresher] Atualização em andamento. Ignorando chamada duplicada.")
            return

        UserCacheRefresher._executing = True
        cacheKey = "GetAllUsersQuery"

        try:
            deleted = await self._cacheService.DeleteAsync(cacheKey)
            if deleted:
                self._logger.info(f"[CACHE] Lista '{cacheKey}' deletada com sucesso.")
            else:
                self._logger.info(f"[CACHE] Lista '{cacheKey}' não existia.")

            # CUIDADO: esse GetAll não pode disparar eventos!
            users = await self._repository.GetAll()
            serialized_users = [UserQueryModel.from_entity(u).model_dump() for u in users]

            await self._cacheService.SetAsync(cacheKey, serialized_users)
            self._logger.info(f"[CACHE] Lista '{cacheKey}' atualizada com {len(serialized_users)} usuários.")

        except Exception as ex:
            self._logger.error(f"[ERROR] Falha ao atualizar cache '{cacheKey}': {ex}")

        finally:
            UserCacheRefresher._executing = False
