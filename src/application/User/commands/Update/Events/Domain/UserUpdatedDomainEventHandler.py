# src/application/User/events/UserUpdatedDomainEventHandler.py

from domain.entities.User.events.UserUpdatedDomainEvent import UserUpdatedDomainEvent

class UserUpdatedDomainEventHandler:
    def __init__(self, logger=None):
        self._logger = logger

    async def Handle(self, event: UserUpdatedDomainEvent):
        if self._logger:
            self._logger.info(f"[EVENT] UserUpdatedDomainEvent: {event.Name} ({event.Email})")
        else:
            print(f"[EVENT] UserUpdatedDomainEvent: {event.Name} ({event.Email})")
