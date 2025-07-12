# src/application/User/commands/Create/Events/Messaging/RabbitMQ/UserCreatedRabbitMQEventHandler.py

from domain.entities.User.events.UserCreatedDomainEvent import UserCreatedDomainEvent
from infrastructure.messaging.User.Pub.RabbitMQPublisher import RabbitMQPublisher

class UserCreatedRabbitMQEventHandler:
    def __init__(self, logger=None):
        self._logger = logger
        self._publisher = RabbitMQPublisher()

    async def Handle(self, event: UserCreatedDomainEvent):
        message = {
            "Id": event.Id,
            "Name": event.Name,
            "Email": event.Email,
            "Phone": event.Phone,
            "Notification": str(event.Notification),
            "Gender": str(event.Gender)
        }

        self._publisher.publish(message)

        if self._logger:
            self._logger.info(f"[RABBITMQ] UserCreated event published for {event.Name}")
        else:
            print(f"[RABBITMQ] UserCreated event published for {event.Name}")
