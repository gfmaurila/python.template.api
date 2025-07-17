from fastapi import APIRouter, HTTPException, status
from application.User.dtos.UserDto import UserDto
from infrastructure.repositories.UserRepository import UserRepository  
from application.User.commands.Create.CreateUserCommand import CreateUserCommand
from application.User.commands.Update.UpdateUserCommand import UpdateUserCommand
from application.User.commands.Delete.Events.DeleteUserCommand import DeleteUserCommand
from application.User.queries.GetUserByIdQuery import GetUserByIdQuery
from application.User.queries.GetAllUsersQuery import GetAllUsersQuery
from core.response.Responses import ApiResult, ErrorDetail

router = APIRouter()
repository = UserRepository()  # <-- Ajustado

@router.post("/users", response_model=ApiResult[dict])
async def CreateUser(dto: UserDto):
    try:
        command = CreateUserCommand(repository)
        user = await command.Handle(dto)
        return ApiResult.create_success({"id": user.Id}, "Usuário criado com sucesso!")
    except Exception as ex:
        return ApiResult.create_error(
            [ErrorDetail(message=str(ex))],
            status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@router.get("/users", response_model=ApiResult[list])
async def GetAllUsers():
    try:
        query = GetAllUsersQuery(repository)
        users = await query.Handle()
        return ApiResult.create_success(users, "Usuários carregados com sucesso.")
    except Exception as ex:
        return ApiResult.create_error(
            [ErrorDetail(message=str(ex))],
            status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@router.get("/users/{userId}", response_model=ApiResult[dict])
async def GetUser(userId: int):
    try:
        query = GetUserByIdQuery(repository)
        user = await query.Handle(userId)
        if not user:
            return ApiResult.create_error(
                [ErrorDetail(message="Usuário não encontrado.")],
                status.HTTP_404_NOT_FOUND
            )
        return ApiResult.create_success(user)
    except Exception as ex:
        return ApiResult.create_error(
            [ErrorDetail(message=str(ex))],
            status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@router.put("/users/{userId}", response_model=ApiResult[None])
async def UpdateUser(userId: int, dto: UserDto):
    try:
        command = UpdateUserCommand(repository)
        await command.Handle(userId, dto)
        return ApiResult.create_success(None, "Usuário atualizado com sucesso.")
    except Exception as ex:
        return ApiResult.create_error(
            [ErrorDetail(message=str(ex))],
            status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@router.delete("/users/{userId}", response_model=ApiResult[None])
async def DeleteUser(userId: int):
    try:
        command = DeleteUserCommand(repository)
        await command.Handle(userId)
        return ApiResult.create_success(None, "Usuário excluído com sucesso.")
    except Exception as ex:
        return ApiResult.create_error(
            [ErrorDetail(message=str(ex))],
            status.HTTP_500_INTERNAL_SERVER_ERROR
        )
