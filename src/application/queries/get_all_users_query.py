
# application/queries/get_all_users_query.py



from domain.interfaces.user_repository import IUserRepository

class GetAllUsersQuery:
    def __init__(self, repository: IUserRepository):
        self.repository = repository

    async def handle(self):
        return await self.repository.get_all()




