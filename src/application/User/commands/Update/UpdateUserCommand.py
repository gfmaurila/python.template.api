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
        self.repository = repository

    async def Handle(self, userId: int, dto: UserDto) -> None:
        existingUser = await self.repository.GetById(userId)
        if not existingUser:
            raise HTTPException(status_code=404, detail="User not found")

        userWithEmail = await self.repository.GetByEmail(dto.Email)
        if userWithEmail and userWithEmail.Id != userId:
            raise HTTPException(status_code=400, detail="Email already in use by another user")

        user = UserEntity(
            Id=userId,
            Name=dto.Name,
            Email=Email(dto.Email),
            Senha=dto.Senha,
            Phone=PhoneNumber(dto.Phone),
            Notification=dto.Notification,
            Gender=dto.Gender
        )

        await self.repository.Update(userId, user)

        event = UserUpdatedDomainEvent(
            userId=user.Id,
            name=user.Name,
            email=user.Email.address,
            phone=user.Phone.phone,
            notification=user.Notification,
            gender=user.Gender
        )

        handler = UserUpdatedDomainEventHandler()
        await handler.Handle(event)
