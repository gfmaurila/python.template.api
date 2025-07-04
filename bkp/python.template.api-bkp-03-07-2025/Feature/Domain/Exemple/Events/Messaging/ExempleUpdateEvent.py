from uuid import UUID, uuid4

from Feature.Domain.Exemple.Events.ExempleBaseEvent import ExempleBaseEvent
from Feature.Exemple.Commands.Update.UpdateExempleCommand import UpdateExempleCommand
from Feature.Domain.Exemple.Models.AuthExempleCreateUpdateDeleteModel import AuthExempleCreateUpdateDeleteModel


class ExempleUpdateEvent(ExempleBaseEvent):
    """
    Represents an event triggered when an Exemple entity is updated.
    """

    def __init__(self,
                 id: UUID,
                 request: UpdateExempleCommand,
                 model: AuthExempleCreateUpdateDeleteModel):
        super().__init__(
            Id=id,
            FirstName=request.FirstName,
            LastName=request.LastName,
            Gender=request.Gender,
            Notification=request.Notification,
            Email=request.Email,
            Phone=request.Phone,
            Role=request.Role,
            Status=request.Status,
            DtInsert=model.DtInsert,
            DtInsertId=model.DtInsertId,
            DtUpdate=model.DtUpdate,
            DtUpdateId=model.DtUpdateId,
            DtDelete=model.DtDelete,
            DtDeleteId=model.DtDeleteId
        )

        self.AggregateId = uuid4()
        self.MessageType = self.__class__.__name__
