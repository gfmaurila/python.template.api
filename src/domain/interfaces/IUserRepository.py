# src/domain/interfaces/IUserRepository.py

from abc import ABC, abstractmethod
from typing import List, Optional
from domain.entities.User.UserEntity import UserEntity

class IUserRepository(ABC):
    @abstractmethod
    async def Add(self, user: UserEntity) -> None:
        ...

    @abstractmethod
    async def GetAll(self) -> List[UserEntity]:
        ...

    @abstractmethod
    async def GetById(self, userId: int) -> Optional[UserEntity]:
        ...

    @abstractmethod
    async def Update(self, userId: int, user: UserEntity) -> None:
        ...

    @abstractmethod
    async def Delete(self, userId: int) -> None:
        ...

    @abstractmethod
    async def Exists(self, userId: int) -> bool:
        ...

    @abstractmethod
    async def GetByEmail(self, email: str) -> Optional[UserEntity]:
        ...

    @abstractmethod
    async def Exists(self, userId: int) -> bool:
        ...
