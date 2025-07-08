# src/domain/events/UserUpdatedDomainEvent.py

from core.domain.events.Event import Event
from domain.enums.EGender import EGender
from domain.enums.ENotificationType import ENotificationType

class UserUpdatedDomainEvent(Event):
    def __init__(self, userId: int, name: str, email: str, phone: str, notification: ENotificationType, gender: EGender):
        super().__init__()
        self.Id = userId
        self.Name = name
        self.Email = email
        self.Phone = phone
        self.Notification = notification
        self.Gender = gender
