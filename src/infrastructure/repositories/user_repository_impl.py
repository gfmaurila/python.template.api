
# src/infrastructure/repositories/user_repository_impl.py

from typing import List
from domain.entities.user import User
from domain.interfaces.user_repository import IUserRepository

class UserRepositoryMemory(IUserRepository):
    def __init__(self):
        self._users: List[User] = []
        self._next_id = 1

    async def add(self, user: User) -> None:
        user.id = self._next_id
        self._next_id += 1
        self._users.append(user)

    async def get_all(self) -> List[User]:
        return self._users

    async def get_by_id(self, user_id: int) -> User:
        return next((u for u in self._users if u.id == user_id), None)

    async def update(self, user_id: int, updated_user: User) -> None:
        for i, user in enumerate(self._users):
            if user.id == user_id:
                self._users[i].name = updated_user.name
                self._users[i].email = updated_user.email

    async def delete(self, user_id: int) -> None:
        self._users = [u for u in self._users if u.id != user_id]


