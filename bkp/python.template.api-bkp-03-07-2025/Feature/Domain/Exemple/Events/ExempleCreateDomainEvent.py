from uuid import UUID
from Feature.Domain.Exemple.Models.AuthExempleCreateUpdateDeleteModel import AuthExempleCreateUpdateDeleteModel
from Feature.Exemple.Commands.Create.CreateExempleCommand import CreateExempleCommand
from Feature.Domain.Exemple.Events.ExempleBaseEvent import ExempleBaseEvent


class ExempleCreateDomainEvent(ExempleBaseEvent):
    """
    Represents a domain event triggered when a new Exemple entity is created.
    """

    def __init__(self,
                 Id: UUID,
                 request: CreateExempleCommand,
                 model: AuthExempleCreateUpdateDeleteModel):
        super().__init__(
            Id=Id,
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
