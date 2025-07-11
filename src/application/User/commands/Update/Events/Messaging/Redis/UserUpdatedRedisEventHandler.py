from domain.entities.User.events.UserUpdatedDomainEvent import UserUpdatedDomainEvent
from infrastructure.messaging.RedisPublisher import RedisPublisher

class UserUpdatedRedisEventHandler:
    def __init__(self):
        self._publisher = RedisPublisher()

    async def Handle(self, event: UserUpdatedDomainEvent):
        message = {
            "Id": event.Id,
            "Name": event.Name,
            "Email": event.Email,
            "Phone": event.Phone,
            "Notification": str(event.Notification),
            "Gender": str(event.Gender)
        }

        self._publisher.publish("user-updated", message)
