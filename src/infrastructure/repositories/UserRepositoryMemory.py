
# src/infrastructure/repositories/user_repository_impl.py

from typing import List
from domain.entities.User import User
from domain.interfaces.IUserRepository import IUserRepository

class UserRepositoryMemory(IUserRepository):
    def __init__(self):
        self._users: List[User] = []
        self._nextId = 1

    async def Add(self, user: User) -> None:
        user.Id = self._nextId
        self._nextId += 1
        self._users.append(user)

    async def GetAll(self) -> List[User]:
        return self._users

    async def GetById(self, userId: int) -> User:
        return next((u for u in self._users if u.Id == userId), None)

    async def Update(self, userId: int, updatedUser: User) -> None:
        for i, user in enumerate(self._users):
            if user.Id == userId:
                self._users[i].Name = updatedUser.Name
                self._users[i].Email = updatedUser.Email

    async def Delete(self, userId: int) -> None:
        self._users = [u for u in self._users if u.Id != userId]


