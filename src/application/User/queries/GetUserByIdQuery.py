# src/application/User/queries/GetUserByIdQuery.py

from domain.interfaces.IUserRepository import IUserRepository
from application.User.dtos.UserQueryModel import UserQueryModel

class GetUserByIdQuery:
    def __init__(self, repository: IUserRepository):
        self._repository = repository

    async def Handle(self, userId: int):
        user = await self._repository.GetById(userId)
        return UserQueryModel.from_entity(user) if user else None
