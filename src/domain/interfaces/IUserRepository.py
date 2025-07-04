
# src/domain/interfaces/user_repository.py

from typing import List
from domain.entities.User import User

class IUserRepository:
    async def Add(self, user: User) -> None:
        raise NotImplementedError

    async def GetAll(self) -> List[User]:
        raise NotImplementedError

    async def GetById(self, userId: int) -> User:
        raise NotImplementedError

    async def Update(self, userId: int, user: User) -> None:
        raise NotImplementedError

    async def Delete(self, userId: int) -> None:
        raise NotImplementedError
