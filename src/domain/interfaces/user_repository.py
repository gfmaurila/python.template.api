
# src/domain/interfaces/user_repository.py

from typing import List
from domain.entities.user import User

class IUserRepository:
    async def add(self, user: User) -> None:
        raise NotImplementedError

    async def get_all(self) -> List[User]:
        raise NotImplementedError

    async def get_by_id(self, user_id: int) -> User:
        raise NotImplementedError

    async def update(self, user_id: int, user: User) -> None:
        raise NotImplementedError

    async def delete(self, user_id: int) -> None:
        raise NotImplementedError
