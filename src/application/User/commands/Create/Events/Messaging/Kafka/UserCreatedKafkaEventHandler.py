# src/application/User/commands/Create/Events/Messaging/Kafka/UserCreatedKafkaEventHandler.py

from infrastructure.messaging.User.Pub.KafkaPublisher import KafkaPublisher

class UserCreatedKafkaEventHandler:
    async def Handle(self, event):
        message = {
            "event": "UserCreated",
            "data": {
                "id": event.Id,
                "name": event.Name,
                "email": event.Email
            }
        }
        KafkaPublisher().publish(message)


