# src/application/User/commands/DeleteUserCommand.py

from fastapi import HTTPException
from domain.interfaces.IUserRepository import IUserRepository
from domain.entities.User.events.UserDeletedDomainEvent import UserDeletedDomainEvent
from application.User.commands.Delete.Events.Domain.UserDeletedDomainEventHandler import UserDeletedDomainEventHandler
from application.User.commands.Delete.Events.Messaging.Redis.UserDeletedRedisEventHandler import UserDeletedRedisEventHandler

class DeleteUserCommand:
    def __init__(self, repository: IUserRepository):
        self._repository = repository

    async def Handle(self, userId: int) -> None:
        # Buscar o usuário antes de deletar
        user = await self._repository.GetById(userId)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        # Criar evento de domínio
        event = UserDeletedDomainEvent(
            userId=user.Id,
            name=user.Name,
            email=user.Email.address
        )

        # Processar eventos
        handler = UserDeletedDomainEventHandler()
        await handler.Handle(event)

        # RedisPublisher
        redisHandler = UserDeletedRedisEventHandler()
        await redisHandler.Handle(event)

        # Executar exclusão
        await self._repository.Delete(userId)

        
