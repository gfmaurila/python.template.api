from domain.entities.User.UserEntity import UserEntity
from application.User.dtos.UserDto import UserDto
from domain.interfaces.IUserRepository import IUserRepository
from domain.valueobjects.Email import Email
from domain.valueobjects.PhoneNumber import PhoneNumber
from application.User.commands.events.UserCreatedDomainEventHandler import UserCreatedDomainEventHandler

class CreateUserCommand:
    def __init__(self, repository: IUserRepository):
        self._repository = repository

    async def Handle(self, dto: UserDto) -> UserEntity:
        user = UserEntity(
            Id=0,
            Name=dto.Name,
            Email=Email(dto.Email),
            Senha=dto.Senha,
            Phone=PhoneNumber(dto.Phone),
            Notification=dto.Notification,
            Gender=dto.Gender
        )

        await self._repository.Add(user)

        # Processa eventos de domínio
        for event in user.DomainEvents:
            handler = UserCreatedDomainEventHandler()
            await handler.Handle(event)

        user.ClearDomainEvents()

        return user
