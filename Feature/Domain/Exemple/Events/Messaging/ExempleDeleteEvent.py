from uuid import UUID, uuid4
from typing import List

from Feature.Domain.Exemple.Events.ExempleBaseEvent import ExempleBaseEvent
from Common.Domain.Enumerado.EGender import EGender
from Common.Domain.Enumerado.ENotificationType import ENotificationType


class ExempleDeleteEvent(ExempleBaseEvent):
    """
    Represents an event triggered when an Exemple entity is deleted.
    """

    def __init__(self,
                 id: UUID,
                 first_name: str,
                 last_name: str,
                 gender: EGender,
                 notification: ENotificationType,
                 email: str,
                 phone: str,
                 role: List[str]):
        super().__init__(
            Id=id,
            FirstName=first_name,
            LastName=last_name,
            Gender=gender,
            Notification=notification,
            Email=email,
            Phone=phone,
            Role=role
        )
        self.AggregateId = uuid4()
        self.MessageType = self.__class__.__name__
