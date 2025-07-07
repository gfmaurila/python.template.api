# src/application/User/commands/UpdateUserCommand.py

from domain.entities.User import User
from application.User.dtos.UserDto import UserDto
from domain.interfaces.IUserRepository import IUserRepository
from domain.valueobjects.Email import Email
from domain.valueobjects.PhoneNumber import PhoneNumber

class UpdateUserCommand:
    def __init__(self, repository: IUserRepository):
        self._repository = repository

    async def Handle(self, userId: int, dto: UserDto):
        user = User(
            Id=userId,
            Name=dto.Name,
            Email=Email(dto.Email),
            Senha=dto.Senha,
            Phone=PhoneNumber(dto.Phone),
            Notification=dto.Notification,
            Gender=dto.Gender
        )
        await self._repository.Update(userId, user)
