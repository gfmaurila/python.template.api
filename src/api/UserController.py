# from typing import Optional
# from fastapi import APIRouter, HTTPException, Query, status, Depends
# from application.User.dtos.UserDto import UserDto
# from application.User.dtos.UserFilterDto import UserFilterDto
# from application.User.dtos.UserQueryModel import UserQueryModel
# from application.User.queries import GetPagedUsersQuery
# from core.dependencies.gender_parser import parse_gender
# from core.domain.model.PagedResponse import PagedResponse
# from domain.enums.EGender import EGender
# from infrastructure.repositories.UserRepository import UserRepository
# from application.User.commands.Create.CreateUserCommand import CreateUserCommand
# from application.User.commands.Update.UpdateUserCommand import UpdateUserCommand
# from application.User.commands.Delete.Events.DeleteUserCommand import DeleteUserCommand
# from application.User.queries.GetUserByIdQuery import GetUserByIdQuery
# from application.User.queries.GetAllUsersQuery import GetAllUsersQuery
# from core.response.Responses import ApiResult, ErrorDetail
# from loguru import logger
# from core.security.Security import get_current_user


# router = APIRouter(
#     prefix="/users",
#     tags=["Users"]
# )

# repository = UserRepository()

# @router.post("", response_model=ApiResult[dict])
# async def CreateUser(dto: UserDto, user=Depends(get_current_user)):
#     try:
#         command = CreateUserCommand(repository)
#         userCreated = await command.Handle(dto)
#         logger.info("Ação: POST /users - Usuário criado com sucesso | ID: {} | Nome: {}", userCreated.Id, dto.Name)
#         return ApiResult.create_success({"id": userCreated.Id}, "Usuário criado com sucesso!")
#     except Exception as ex:
#         logger.error("Erro ao criar usuário: {}", str(ex))
#         return ApiResult.create_error(
#             [ErrorDetail(message=str(ex))],
#             status.HTTP_500_INTERNAL_SERVER_ERROR
#         )

# @router.get("", response_model=ApiResult[list])
# async def GetAllUsers(user=Depends(get_current_user)):
#     try:
#         query = GetAllUsersQuery(repository)
#         users = await query.Handle()
#         logger.info("Ação: GET /users - {} usuários carregados", len(users))
#         return ApiResult.create_success(users, "Usuários carregados com sucesso.")
#     except Exception as ex:
#         logger.error("Erro ao carregar usuários: {}", str(ex))
#         return ApiResult.create_error(
#             [ErrorDetail(message=str(ex))],
#             status.HTTP_500_INTERNAL_SERVER_ERROR
#         )

# @router.get("/{userId}", response_model=ApiResult[dict])
# async def GetUser(userId: int, user=Depends(get_current_user)):
#     try:
#         query = GetUserByIdQuery(repository)
#         userFound = await query.Handle(userId)
#         if not userFound:
#             logger.warning("Ação: GET /users/{} - Usuário não encontrado", userId)
#             return ApiResult.create_error(
#                 [ErrorDetail(message="Usuário não encontrado.")],
#                 status.HTTP_404_NOT_FOUND
#             )
#         logger.info("Ação: GET /users/{} - Usuário carregado", userId)
#         return ApiResult.create_success(userFound.model_dump())
#     except Exception as ex:
#         logger.error("Erro ao obter usuário {}: {}", userId, str(ex))
#         return ApiResult.create_error(
#             [ErrorDetail(message=str(ex))],
#             status.HTTP_500_INTERNAL_SERVER_ERROR
#         )

# @router.put("/{userId}", response_model=ApiResult[None])
# async def UpdateUser(userId: int, dto: UserDto, user=Depends(get_current_user)):
#     try:
#         command = UpdateUserCommand(repository)
#         await command.Handle(userId, dto)
#         logger.info("Ação: PUT /users/{} - Usuário atualizado com sucesso | Nome: {}", userId, dto.Name)
#         return ApiResult.create_success(None, "Usuário atualizado com sucesso.")
#     except Exception as ex:
#         logger.error("Erro ao atualizar usuário {}: {}", userId, str(ex))
#         return ApiResult.create_error(
#             [ErrorDetail(message=str(ex))],
#             status.HTTP_500_INTERNAL_SERVER_ERROR
#         )

# @router.delete("/{userId}", response_model=ApiResult[None])
# async def DeleteUser(userId: int, user=Depends(get_current_user)):
#     try:
#         command = DeleteUserCommand(repository)
#         await command.Handle(userId)
#         logger.info("Ação: DELETE /users/{} - Usuário excluído com sucesso", userId)
#         return ApiResult.create_success(None, "Usuário excluído com sucesso.")
#     except Exception as ex:
#         logger.error("Erro ao excluir usuário {}: {}", userId, str(ex))
#         return ApiResult.create_error(
#             [ErrorDetail(message=str(ex))],
#             status.HTTP_500_INTERNAL_SERVER_ERROR
#         )

# @router.get("/paged", response_model=PagedResponse[UserQueryModel])
# async def GetPagedUsers(
#     name: Optional[str] = Query(None),
#     email: Optional[str] = Query(None),
#     page: int = Query(1),
#     pageSize: int = Query(10)
# ):
#     filterDto = UserFilterDto(
#         Name=name,
#         Email=email,
#         Page=page,
#         PageSize=pageSize
#     )

#     repository = UserRepository()
#     query = GetPagedUsersQuery(repository)
#     return await query.Handle(filterDto)
    


from typing import Optional
from fastapi import APIRouter, HTTPException, Query, status, Depends
from application.User.dtos.UserDto import UserDto
from application.User.dtos.UserFilterDto import UserFilterDto
from application.User.dtos.UserQueryModel import UserQueryModel
from application.User.queries.GetPagedUsersQuery import GetPagedUsersQuery
from core.domain.model.PagedResponse import PagedResponse
from infrastructure.repositories.UserRepository import UserRepository
from application.User.commands.Create.CreateUserCommand import CreateUserCommand
from application.User.commands.Update.UpdateUserCommand import UpdateUserCommand
from application.User.commands.Delete.Events.DeleteUserCommand import DeleteUserCommand
from application.User.queries.GetUserByIdQuery import GetUserByIdQuery
from application.User.queries.GetAllUsersQuery import GetAllUsersQuery
from core.response.Responses import ApiResult, ErrorDetail
from loguru import logger
from core.security.Security import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

repository = UserRepository()

@router.post("", response_model=ApiResult[dict])
async def CreateUser(dto: UserDto, user=Depends(get_current_user)):
    try:
        command = CreateUserCommand(repository)
        userCreated = await command.Handle(dto)
        logger.info("Ação: POST /users - Usuário criado com sucesso | ID: {} | Nome: {}", userCreated.Id, dto.Name)
        return ApiResult.create_success({"id": userCreated.Id}, "Usuário criado com sucesso!")
    except Exception as ex:
        logger.error("Erro ao criar usuário: {}", str(ex))
        return ApiResult.create_error(
            [ErrorDetail(message=str(ex))],
            status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@router.get("", response_model=ApiResult[list])
async def GetAllUsers(user=Depends(get_current_user)):
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

# Coloque a rota /paged ANTES da rota /{userId}
@router.get("/paged", response_model=PagedResponse[UserQueryModel])
async def GetPagedUsers(
    name: Optional[str] = Query(None),
    email: Optional[str] = Query(None),
    page: int = Query(1),
    pageSize: int = Query(10)
):
    try:
        filterDto = UserFilterDto(
            Name=name,
            Email=email,
            Page=page,
            PageSize=pageSize
        )

        query = GetPagedUsersQuery(repository)
        result = await query.Handle(filterDto)
        logger.info("Ação: GET /users/paged - Página {} carregada", page)
        return result
    except Exception as ex:
        logger.error("Erro ao paginar usuários: {}", str(ex))
        return ApiResult.create_error(
            [ErrorDetail(message=str(ex))],
            status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@router.get("/{userId}", response_model=ApiResult[dict])
async def GetUser(userId: int, user=Depends(get_current_user)):
    try:
        query = GetUserByIdQuery(repository)
        userFound = await query.Handle(userId)
        if not userFound:
            logger.warning("Ação: GET /users/{} - Usuário não encontrado", userId)
            return ApiResult.create_error(
                [ErrorDetail(message="Usuário não encontrado.")],
                status.HTTP_404_NOT_FOUND
            )
        logger.info("Ação: GET /users/{} - Usuário carregado", userId)
        return ApiResult.create_success(userFound.model_dump())
    except Exception as ex:
        logger.error("Erro ao obter usuário {}: {}", userId, str(ex))
        return ApiResult.create_error(
            [ErrorDetail(message=str(ex))],
            status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@router.put("/{userId}", response_model=ApiResult[None])
async def UpdateUser(userId: int, dto: UserDto, user=Depends(get_current_user)):
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

@router.delete("/{userId}", response_model=ApiResult[None])
async def DeleteUser(userId: int, user=Depends(get_current_user)):
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
