from fastapi import APIRouter, HTTPException, status
from application.User.dtos.UserDto import UserDto
from infrastructure.repositories.UserRepository import UserRepository
from application.User.commands.Create.CreateUserCommand import CreateUserCommand
from application.User.commands.Update.UpdateUserCommand import UpdateUserCommand
from application.User.commands.Delete.Events.DeleteUserCommand import DeleteUserCommand
from application.User.queries.GetUserByIdQuery import GetUserByIdQuery
from application.User.queries.GetAllUsersQuery import GetAllUsersQuery
from core.response.Responses import ApiResult, ErrorDetail
from loguru import logger

router = APIRouter()
repository = UserRepository()

@router.post("/users", response_model=ApiResult[dict])
async def CreateUser(dto: UserDto):
    try:
        command = CreateUserCommand(repository)
        user = await command.Handle(dto)
        logger.info("Ação: POST /users - Usuário criado com sucesso | ID: {} | Nome: {}", user.Id, dto.Name)
        return ApiResult.create_success({"id": user.Id}, "Usuário criado com sucesso!")
    except Exception as ex:
        logger.error("Erro ao criar usuário: {}", str(ex))
        return ApiResult.create_error(
            [ErrorDetail(message=str(ex))],
            status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@router.get("/users", response_model=ApiResult[list])
async def GetAllUsers():
    try:
        query = GetAllUsersQuery(repository)
        users = await query.Handle()
        logger.info("Ação: GET /users - {} usuários carregados", len(users))
        return ApiResult.create_success(users, "Usuários carregados com sucesso.")
    except Exception as ex:
        logger.error("Erro ao carregar usuários: {}", str(ex))
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
            logger.warning("Ação: GET /users/{} - Usuário não encontrado", userId)
            return ApiResult.create_error(
                [ErrorDetail(message="Usuário não encontrado.")],
                status.HTTP_404_NOT_FOUND
            )
        logger.info("Ação: GET /users/{} - Usuário carregado", userId)
        return ApiResult.create_success(user.model_dump())
    except Exception as ex:
        logger.error("Erro ao obter usuário {}: {}", userId, str(ex))
        return ApiResult.create_error(
            [ErrorDetail(message=str(ex))],
            status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@router.put("/users/{userId}", response_model=ApiResult[None])
async def UpdateUser(userId: int, dto: UserDto):
    try:
        command = UpdateUserCommand(repository)
        await command.Handle(userId, dto)
        logger.info("Ação: PUT /users/{} - Usuário atualizado com sucesso | Nome: {}", userId, dto.Name)
        return ApiResult.create_success(None, "Usuário atualizado com sucesso.")
    except Exception as ex:
        logger.error("Erro ao atualizar usuário {}: {}", userId, str(ex))
        return ApiResult.create_error(
            [ErrorDetail(message=str(ex))],
            status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@router.delete("/users/{userId}", response_model=ApiResult[None])
async def DeleteUser(userId: int):
    try:
        command = DeleteUserCommand(repository)
        await command.Handle(userId)
        logger.info("Ação: DELETE /users/{} - Usuário excluído com sucesso", userId)
        return ApiResult.create_success(None, "Usuário excluído com sucesso.")
    except Exception as ex:
        logger.error("Erro ao excluir usuário {}: {}", userId, str(ex))
        return ApiResult.create_error(
            [ErrorDetail(message=str(ex))],
            status.HTTP_500_INTERNAL_SERVER_ERROR
        )
