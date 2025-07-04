
# src/api/user_controller.py


from fastapi import APIRouter
from application.commands.create_user_command import CreateUserCommand
from application.queries.get_user_query import GetUserQuery
from infrastructure.repositories.user_repository_impl import UserRepositoryMemory
from application.dtos.user_dto import UserDTO

router = APIRouter()
repository = UserRepositoryMemory()
create_user = CreateUserCommand(repository)
get_user = GetUserQuery(repository)

@router.post("/users")
async def create_user_endpoint(dto: UserDTO):
    return await create_user.handle(dto)

@router.get("/users/{user_id}")
async def get_user_endpoint(user_id: int):
    return await get_user.handle(user_id)


