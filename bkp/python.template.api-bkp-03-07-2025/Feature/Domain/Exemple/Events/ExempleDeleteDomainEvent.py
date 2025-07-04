from typing import List
from uuid import UUID
from Common.Domain.Enumerado.EGender import EGender
from Common.Domain.Enumerado.ENotificationType import ENotificationType
from Feature.Domain.Exemple.Events.ExempleBaseEvent import ExempleBaseEvent


class ExempleDeleteDomainEvent(ExempleBaseEvent):
    """
    Represents a domain event triggered when an Exemple entity is deleted.
    """

    def __init__(self,
                 Id: UUID,
                 FirstName: str,
                 LastName: str,
                 Gender: EGender,
                 Notification: ENotificationType,
                 Email: str,
                 Phone: str,
                 Role: List[str]):
        super().__init__(
            Id=Id,
            FirstName=FirstName,
            LastName=LastName,
            Gender=Gender,
            Notification=Notification,
            Email=Email,
            Phone=Phone,
            Role=Role
        )
