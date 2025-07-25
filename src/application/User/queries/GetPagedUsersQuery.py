# src/application/User/queries/GetPagedUsersQuery.py

from core.domain.model.PagedResponse import PagedResponse
from application.User.dtos.UserQueryModel import UserQueryModel
from application.User.dtos.UserFilterDto import UserFilterDto
from domain.interfaces.IUserRepository import IUserRepository

class GetPagedUsersQuery:
    def __init__(self, repository: IUserRepository):
        self._repository = repository

    async def Handle(self, filter: UserFilterDto) -> PagedResponse[UserQueryModel]:
        users, total = await self._repository.GetPaged(
            name=filter.Name,
            email=filter.Email,
            page=filter.Page,
            page_size=filter.PageSize
        )

        user_models = [UserQueryModel.from_entity(u) for u in users]
        total_pages = (total + filter.PageSize - 1) // filter.PageSize

        return PagedResponse[UserQueryModel](
            TotalItems=total,
            PageSize=filter.PageSize,
            CurrentPage=filter.Page,
            TotalPages=total_pages,
            Items=user_models
        )
