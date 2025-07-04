
# src/application/commands/create_user_command.py

from domain.entities.User import User
from application.dtos.UserDto import UserDto
from domain.interfaces.IUserRepository import IUserRepository

class CreateUserCommand:
    def __init__(self, repository: IUserRepository):
        self._repository = repository

    async def Handle(self, dto: UserDto):
        user = User(Id=0, Name=dto.Name, Email=dto.Email)
        await self._repository.Add(user)
        return user


