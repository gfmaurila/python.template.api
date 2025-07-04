
# src/infrastructure/repositories/user_repository_impl.py

from typing import List
from domain.entities.user import User
from domain.interfaces.user_repository import IUserRepository

class UserRepositoryMemory(IUserRepository):
    def __init__(self):
        self._users: List[User] = []

    async def add(self, user: User) -> None:
        self._users.append(user)

    async def get_all(self) -> List[User]:
        return self._users

    async def get_by_id(self, user_id: int) -> User:
        return next((u for u in self._users if u.id == user_id), None)


