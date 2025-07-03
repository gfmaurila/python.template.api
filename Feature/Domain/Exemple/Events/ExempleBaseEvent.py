from typing import List, Optional
from uuid import UUID, uuid4
from datetime import datetime

from Common.Domain.Events.Event import Event
from Common.Domain.Enumerado.EGender import EGender
from Common.Domain.Enumerado.ENotificationType import ENotificationType


class ExempleBaseEvent(Event):
    """
    Represents the base event class for Exemple-related events.
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
                 Status: bool = True,
                 DtInsert: Optional[datetime] = None,
                 DtInsertId: Optional[int] = None,
                 DtUpdate: Optional[datetime] = None,
                 DtUpdateId: Optional[int] = None,
                 DtDelete: Optional[datetime] = None,
                 DtDeleteId: Optional[int] = None):

        super().__init__("ExempleBaseEvent", uuid4())

        self.Id = Id
        self.FirstName = FirstName
        self.LastName = LastName
        self.Gender = Gender
        self.Notification = Notification
        self.Email = Email
        self.Phone = Phone
        self.Role = Role
        self.Status = Status
        self.DtInsert = DtInsert or datetime.utcnow()
        self.DtInsertId = DtInsertId
        self.DtUpdate = DtUpdate
        self.DtUpdateId = DtUpdateId
        self.DtDelete = DtDelete
        self.DtDeleteId = DtDeleteId

    @classmethod
    def WithAudit(cls,
                  Id: UUID,
                  FirstName: str,
                  LastName: str,
                  Gender: EGender,
                  Notification: ENotificationType,
                  Email: str,
                  Phone: str,
                  Role: List[str],
                  Status: bool,
                  model):
        """
        Factory method to create event using audit model.
        """
        return cls(
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
