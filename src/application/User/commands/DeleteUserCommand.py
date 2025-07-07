# src/application/User/commands/DeleteUserCommand.py

from domain.interfaces.IUserRepository import IUserRepository

class DeleteUserCommand:
    def __init__(self, repository: IUserRepository):
        self._repository = repository

    async def Handle(self, userId: int):
        await self._repository.Delete(userId)
