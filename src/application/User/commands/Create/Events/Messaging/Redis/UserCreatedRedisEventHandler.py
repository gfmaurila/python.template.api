from domain.entities.User.events.UserCreatedDomainEvent import UserCreatedDomainEvent
from infrastructure.messaging.RedisPublisher import RedisPublisher

class UserCreatedRedisEventHandler:
    def __init__(self, logger=None):
        self._logger = logger
        self._publisher = RedisPublisher()

    async def Handle(self, event: UserCreatedDomainEvent):
        message = {
            "Id": event.Id,
            "Name": event.Name,
            "Email": event.Email,
            "Phone": event.Phone,
            "Notification": str(event.Notification),
            "Gender": str(event.Gender)
        }

        self._publisher.publish("user-created", message)

        if self._logger:
            self._logger.info(f"[REDIS] UserCreated event published for {event.Name}")
        else:
            print(f"[REDIS] UserCreated event published for {event.Name}")
