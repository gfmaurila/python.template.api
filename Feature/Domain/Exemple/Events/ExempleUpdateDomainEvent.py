from typing import List
from uuid import UUID
from Common.Domain.Enumerado.EGender import EGender
from Common.Domain.Enumerado.ENotificationType import ENotificationType
from Feature.Domain.Exemple.Models.AuthExempleCreateUpdateDeleteModel import AuthExempleCreateUpdateDeleteModel
from Feature.Domain.Exemple.Events.ExempleBaseEvent import ExempleBaseEvent


class ExempleUpdateDomainEvent(ExempleBaseEvent):
    """
    Represents a domain event triggered when an Exemple entity is updated.
    """

    def __init__(self,
                 Id: UUID,
                 FirstName: str,
                 LastName: str,
                 Gender: EGender,
                 Notification: ENotificationType,
                 Email: str,
                 Phone: str,
                 Role: List[str],
                 Status: bool,
                 model: AuthExempleCreateUpdateDeleteModel):

        super().__init__(
            Id=Id,
            FirstName=FirstName,
            LastName=LastName,
            Gender=Gender,
            Notification=Notification,
            Email=Email,
            Phone=Phone,
            Role=Role,
            Status=Status,
            DtInsert=model.DtInsert,
            DtInsertId=model.DtInsertId,
            DtUpdate=model.DtUpdate,
            DtUpdateId=model.DtUpdateId,
            DtDelete=model.DtDelete,
            DtDeleteId=model.DtDeleteId
        )
