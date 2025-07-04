
# application/queries/get_all_users_query.py



from domain.interfaces.IUserRepository import IUserRepository

class GetAllUsersQuery:
    def __init__(self, repository: IUserRepository):
        self._repository = repository

    async def Handle(self):
        return await self._repository.GetAll()





