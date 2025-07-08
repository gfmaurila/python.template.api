# src/application/User/events/UserDeletedDomainEventHandler.py

from domain.entities.User.events.UserDeletedDomainEvent import UserDeletedDomainEvent

class UserDeletedDomainEventHandler:
    def __init__(self, logger=None):
        self._logger = logger

    async def Handle(self, event: UserDeletedDomainEvent):
        if self._logger:
            self._logger.info(f"[EVENT] UserDeletedDomainEvent triggered for: {event.Name} ({event.Email})")
        else:
            print(f"[EVENT] UserDeletedDomainEvent triggered for: {event.Name} ({event.Email})")
