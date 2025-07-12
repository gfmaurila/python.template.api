from domain.entities.User.events.UserDeletedDomainEvent import UserDeletedDomainEvent
from infrastructure.messaging.User.Pub.RedisPublisher import RedisPublisher

class UserDeletedRedisEventHandler:
    def __init__(self):
        self._publisher = RedisPublisher()

    async def Handle(self, event: UserDeletedDomainEvent):
        message = {
            "Id": event.Id,
            "Name": event.Name,
            "Email": event.Email
        }

        self._publisher.publish("user-deleted", message)
