# src/application/User/queries/GetAllUsersQuery.py

from domain.interfaces.IUserRepository import IUserRepository

class GetAllUsersQuery:
    def __init__(self, repository: IUserRepository):
        self._repository = repository

    async def Handle(self):
        return await self._repository.GetAll()
