
# application/commands/UpdateUserCommand.py

from domain.entities.User import User
from application.dtos.UserDto import UserDto
from domain.interfaces.IUserRepository import IUserRepository

class UpdateUserCommand:
    def __init__(self, repository: IUserRepository):
        self._repository = repository

    async def Handle(self, userId: int, dto: UserDto):
        user = User(Id=userId, Name=dto.Name, Email=dto.Email)
        await self._repository.Update(userId, user)


