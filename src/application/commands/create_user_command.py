
# src/application/commands/create_user_command.py

from domain.entities.user import User
from application.dtos.user_dto import UserDTO
from domain.interfaces.user_repository import IUserRepository

class CreateUserCommand:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    async def handle(self, user_dto: UserDTO):
        user = User(id=1, name=user_dto.name, email=user_dto.email)  # ID estático por enquanto
        await self.user_repository.add(user)
        return user


