from fastapi import HTTPException, status
from core.Config import GetSettings
from domain.entities.User.UserEntity import UserEntity
from application.User.dtos.UserDto import UserDto
from domain.interfaces.IUserRepository import IUserRepository
from domain.valueobjects.Email import Email
from domain.valueobjects.PhoneNumber import PhoneNumber
from application.User.commands.Create.Events.Domain.UserCreatedDomainEventHandler import UserCreatedDomainEventHandler
from application.User.commands.Create.Events.Messaging.Redis.UserCreatedRedisEventHandler import UserCreatedRedisEventHandler
from application.User.commands.Create.Events.Messaging.RabbiMQ.UserCreatedRabbitMQEventHandler import UserCreatedRabbitMQEventHandler

from application.User.commands.Create.Events.Messaging.Kafka.UserCreatedKafkaEventHandler import UserCreatedKafkaEventHandler

from infrastructure.messaging.User.Pub.RabbitMQPublisher import RabbitMQPublisher

settings = GetSettings()

class CreateUserCommand:
    def __init__(self, repository: IUserRepository):
        self._repository = repository

    async def Handle(self, dto: UserDto) -> UserEntity:

        # Verifica se o e-mail já está em uso
        existing_user = await self._repository.GetByEmail(dto.Email)
        if existing_user is not None:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="E-mail já está em uso."
            )

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

            # Event de domain
            handler = UserCreatedDomainEventHandler()
            await handler.Handle(event)

            # RedisPublisher
            redisHandler = UserCreatedRedisEventHandler()
            await redisHandler.Handle(event)

            # RabbitMQPublisher
            rabbitMQEventHandler = UserCreatedRabbitMQEventHandler()
            await rabbitMQEventHandler.Handle(event)

            # KafkaPublisher
            kafkaEventHandler = UserCreatedKafkaEventHandler()
            await kafkaEventHandler.Handle(event)



        user.ClearDomainEvents()

        return user
