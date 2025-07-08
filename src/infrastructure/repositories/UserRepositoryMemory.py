# src/infrastructure/repositories/UserRepositoryMemory.py

from typing import List, Optional
from domain.entities.User.UserEntity import UserEntity
from domain.interfaces.IUserRepository import IUserRepository

class UserRepositoryMemory(IUserRepository):
    def __init__(self):
        self._users: List[UserEntity] = []
        self._nextId = 1

    async def Add(self, user: UserEntity) -> None:
        user.Id = self._nextId
        self._nextId += 1
        self._users.append(user)

    async def GetAll(self) -> List[UserEntity]:
        return self._users

    async def GetById(self, userId: int) -> Optional[UserEntity]:
        return next((u for u in self._users if u.Id == userId), None)

    async def Update(self, userId: int, updatedUser: UserEntity) -> None:
        for i, user in enumerate(self._users):
            if user.Id == userId:
                self._users[i].Name = updatedUser.Name
                self._users[i].Email = updatedUser.Email
                self._users[i].Senha = updatedUser.Senha
                self._users[i].Phone = updatedUser.Phone
                self._users[i].Notification = updatedUser.Notification
                self._users[i].Gender = updatedUser.Gender

    async def Delete(self, userId: int) -> None:
        self._users = [u for u in self._users if u.Id != userId]
