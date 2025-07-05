

# src/application/queries/GetUserByIdQuery.py

from domain.interfaces.IUserRepository import IUserRepository

class GetUserByIdQuery:
    def __init__(self, repository: IUserRepository):
        self._repository = repository

    async def Handle(self, userId: int):
        return await self._repository.GetById(userId)




