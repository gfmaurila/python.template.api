# src/domain/events/UserCreatedDomainEvent.py

from core.domain.events.Event import Event
from domain.enums.EGender import EGender
from domain.enums.ENotificationType import ENotificationType

class UserCreatedDomainEvent(Event):
    def __init__(
        self,
        Id: int,
        Name: str,
        Email: str,
        Phone: str,
        Notification: ENotificationType,
        Gender: EGender
    ):
        super().__init__()
        self.Id = Id
        self.Name = Name
        self.Email = Email
        self.Phone = Phone
        self.Notification = Notification
        self.Gender = Gender
