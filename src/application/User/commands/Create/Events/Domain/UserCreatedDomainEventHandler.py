# src/application/User/events/UserCreatedDomainEventHandler.py

from domain.entities.User.events.UserCreatedDomainEvent import UserCreatedDomainEvent

class UserCreatedDomainEventHandler:
    def __init__(self, logger=None):
        self._logger = logger

    async def Handle(self, event: UserCreatedDomainEvent):
        if self._logger:
            self._logger.info(f"[EVENT] UserCreatedDomainEvent triggered for: {event.Name} ({event.Email})")
        else:
            print(f"[EVENT] UserCreatedDomainEvent triggered for: {event.Name} ({event.Email})")
