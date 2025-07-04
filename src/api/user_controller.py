
# src/api/user_controller.py


from fastapi import APIRouter, HTTPException
from application.dtos.user_dto import UserDTO
from infrastructure.repositories.user_repository_impl import UserRepositoryMemory
from application.commands.create_user_command import CreateUserCommand
from application.commands.update_user_command import UpdateUserCommand
from application.commands.delete_user_command import DeleteUserCommand
from application.queries.get_user_query import GetUserByIdQuery
from application.queries.get_all_users_query import GetAllUsersQuery

router = APIRouter()
repository = UserRepositoryMemory()

@router.post("/users")
async def create_user(dto: UserDTO):
    command = CreateUserCommand(repository)
    return await command.handle(dto)

@router.get("/users")
async def get_all_users():
    query = GetAllUsersQuery(repository)
    return await query.handle()

@router.get("/users/{user_id}")
async def get_user(user_id: int):
    query = GetUserByIdQuery(repository)
    user = await query.handle(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/users/{user_id}")
async def update_user(user_id: int, dto: UserDTO):
    command = UpdateUserCommand(repository)
    await command.handle(user_id, dto)
    return {"message": "User updated"}

@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    command = DeleteUserCommand(repository)
    await command.handle(user_id)
    return {"message": "User deleted"}


