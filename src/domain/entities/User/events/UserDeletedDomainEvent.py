# src/domain/events/UserDeletedDomainEvent.py

from core.domain.events.Event import Event

class UserDeletedDomainEvent(Event):
    def __init__(self, userId: int, name: str, email: str):
        super().__init__()
        self.Id = userId
        self.Name = name
        self.Email = email
