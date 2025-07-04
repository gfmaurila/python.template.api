
# src/application/commands/create_user_command.py

from domain.entities.user import User
from application.dtos.user_dto import UserDTO
from domain.interfaces.user_repository import IUserRepository

class CreateUserCommand:
    def __init__(self, repository: IUserRepository):
        self.repository = repository

    async def handle(self, dto: UserDTO):
        user = User(id=0, name=dto.name, email=dto.email)
        await self.repository.add(user)
        return user


