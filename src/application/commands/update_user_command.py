
# application/commands/update_user_command.py

from domain.entities.user import User
from application.dtos.user_dto import UserDTO
from domain.interfaces.user_repository import IUserRepository

class UpdateUserCommand:
    def __init__(self, repository: IUserRepository):
        self.repository = repository

    async def handle(self, user_id: int, dto: UserDTO):
        user = User(id=user_id, name=dto.name, email=dto.email)
        await self.repository.update(user_id, user)


