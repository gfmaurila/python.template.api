
# src/api/user_controller.py


from fastapi import APIRouter, HTTPException
from application.dtos.UserDto import UserDto
from infrastructure.repositories.UserRepositoryMemory import UserRepositoryMemory
from application.commands.User.CreateUserCommand import CreateUserCommand
from application.commands.User.UpdateUserCommand import UpdateUserCommand
from application.commands.User.DeleteUserCommand import DeleteUserCommand
from application.queries.User.GetUserByIdQuery import GetUserByIdQuery
from application.queries.User.GetAllUsersQuery import GetAllUsersQuery

router = APIRouter()
repository = UserRepositoryMemory()

@router.post("/users")
async def CreateUser(dto: UserDto):
    command = CreateUserCommand(repository)
    return await command.Handle(dto)

@router.get("/users")
async def GetAllUsers():
    query = GetAllUsersQuery(repository)
    return await query.Handle()

@router.get("/users/{userId}")
async def GetUser(userId: int):
    query = GetUserByIdQuery(repository)
    user = await query.Handle(userId)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/users/{userId}")
async def UpdateUser(userId: int, dto: UserDto):
    command = UpdateUserCommand(repository)
    await command.Handle(userId, dto)
    return {"Message": "User updated"}

@router.delete("/users/{userId}")
async def DeleteUser(userId: int):
    command = DeleteUserCommand(repository)
    await command.Handle(userId)
    return {"Message": "User deleted"}


