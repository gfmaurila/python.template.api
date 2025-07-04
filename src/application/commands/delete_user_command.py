
# application/commands/delete_user_command.py

from domain.interfaces.user_repository import IUserRepository

class DeleteUserCommand:
    def __init__(self, repository: IUserRepository):
        self.repository = repository

    async def handle(self, user_id: int):
        await self.repository.delete(user_id)

