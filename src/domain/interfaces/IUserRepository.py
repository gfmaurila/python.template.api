# src/domain/interfaces/IUserRepository.py

from typing import List, Optional
from domain.entities.User.UserEntity import UserEntity

class IUserRepository:
    async def Add(self, user: UserEntity) -> None:
        """Adiciona um novo usuário ao repositório."""
        raise NotImplementedError

    async def GetAll(self) -> List[UserEntity]:
        """Retorna todos os usuários."""
        raise NotImplementedError

    async def GetById(self, userId: int) -> Optional[UserEntity]:
        """Retorna um usuário pelo ID, ou None se não encontrado."""
        raise NotImplementedError

    async def Update(self, userId: int, user: UserEntity) -> None:
        """Atualiza um usuário existente."""
        raise NotImplementedError

    async def Delete(self, userId: int) -> None:
        """Remove um usuário pelo ID."""
        raise NotImplementedError

    async def Exists(self, userId: int) -> bool:
        """Verifica se o usuário existe pelo ID."""
        raise NotImplementedError