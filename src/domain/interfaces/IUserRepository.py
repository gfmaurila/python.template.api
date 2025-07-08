# src/domain/interfaces/IUserRepository.py

from typing import List
from domain.entities.User.UserEntity import UserEntity

class IUserRepository:
    async def Add(self, user: UserEntity) -> None:
        """Adiciona um novo usuário ao repositório."""
        raise NotImplementedError

    async def GetAll(self) -> List[UserEntity]:
        """Retorna todos os usuários."""
        raise NotImplementedError

    async def GetById(self, userId: int) -> UserEntity:
        """Retorna um usuário pelo ID."""
        raise NotImplementedError

    async def Update(self, userId: int, user: UserEntity) -> None:
        """Atualiza um usuário existente."""
        raise NotImplementedError

    async def Delete(self, userId: int) -> None:
        """Remove um usuário pelo ID."""
        raise NotImplementedError
