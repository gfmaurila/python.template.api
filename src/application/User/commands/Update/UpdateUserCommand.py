from domain.entities.User.UserEntity import UserEntity
from application.User.dtos.UserDto import UserDto
from domain.interfaces.IUserRepository import IUserRepository
from domain.valueobjects.Email import Email
from domain.valueobjects.PhoneNumber import PhoneNumber
from domain.entities.User.events.UserUpdatedDomainEvent import UserUpdatedDomainEvent
from application.User.commands.Update.Events.Domain.UserUpdatedDomainEventHandler import UserUpdatedDomainEventHandler
from fastapi import HTTPException

class UpdateUserCommand:
    def __init__(self, repository: IUserRepository):
        self._repository = repository

    async def Handle(self, userId: int, dto: UserDto) -> None:
        # Verifica se o usuário existe
        existing_user = await self._repository.GetById(userId)
        if not existing_user:
            raise HTTPException(status_code=404, detail="User not found")

        # Cria o novo objeto UserEntity
        user = UserEntity(
            Id=userId,
            Name=dto.Name,
            Email=Email(dto.Email),
            Senha=dto.Senha,
            Phone=PhoneNumber(dto.Phone),
            Notification=dto.Notification,
            Gender=dto.Gender
        )

        # Atualiza no repositório
        await self._repository.Update(userId, user)

        # Gera evento de domínio
        event = UserUpdatedDomainEvent(
            userId=user.Id,
            name=user.Name,
            email=user.Email.address,
            phone=user.Phone.phone,
            notification=user.Notification,
            gender=user.Gender
        )

        # Processa evento
        handler = UserUpdatedDomainEventHandler()
        await handler.Handle(event)
