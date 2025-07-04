

# src/application/queries/get_user_query.py

from domain.interfaces.user_repository import IUserRepository

class GetUserQuery:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    async def handle(self, user_id: int):
        return await self.user_repository.get_by_id(user_id)


