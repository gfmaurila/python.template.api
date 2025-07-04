from uuid import UUID, uuid4
from typing import List
from Common.Domain.BaseEntity import BaseEntity
from Common.Domain.IAggregateRoot import IAggregateRoot
from Common.Domain.ValueObjects.Email import Email
from Common.Domain.ValueObjects.PhoneNumber import PhoneNumber
from Common.Domain.Enumerado.EGender import EGender
from Common.Domain.Enumerado.ENotificationType import ENotificationType
from Feature.Domain.Exemple.Events.ExempleCreateDomainEvent import ExempleCreateDomainEvent
from Feature.Domain.Exemple.Events.ExempleUpdateDomainEvent import ExempleUpdateDomainEvent
from Feature.Domain.Exemple.Events.ExempleDeleteDomainEvent import ExempleDeleteDomainEvent
from Feature.Domain.Exemple.Events.Messaging.ExempleCreateEvent import ExempleCreateEvent
from Feature.Domain.Exemple.Events.Messaging.ExempleUpdateEvent import ExempleUpdateEvent
from Feature.Domain.Exemple.Events.Messaging.ExempleDeleteEvent import ExempleDeleteEvent


class ExempleEntity(BaseEntity, IAggregateRoot):
    """
    Represents an example entity that follows the aggregate root pattern.
    """

    def __init__(self, request, model):
        super().__init__()
        self.Id = uuid4()
        self.FirstName = request.FirstName
        self.LastName = request.LastName
        self.Gender = request.Gender
        self.Notification = request.Notification
        self.Email = Email(request.Email)
        self.Phone = PhoneNumber(request.Phone)
        self.Role = request.Role
        self.Status = request.Status
        self.DtInsert = model.DtInsert
        self.DtInsertId = model.DtInsertId

        # Domain and integration events
        self.AddDomainEvent(ExempleCreateDomainEvent(
            self.Id, request, model))

        self.AddDomainEvent(ExempleCreateEvent(
            self.Id, request, model))

    def Update(self, command, model):
        self.FirstName = command.FirstName
        self.LastName = command.LastName
        self.Gender = command.Gender
        self.Notification = command.Notification
        self.Email = Email(command.Email)
        self.Phone = PhoneNumber(command.Phone)
        self.Role = command.Role
        self.Status = command.Status
        self.DtUpdate = model.DtUpdate
        self.DtUpdateId = model.DtUpdateId

        self.AddDomainEvent(ExempleUpdateDomainEvent(
            self.Id,
            command.FirstName,
            command.LastName,
            command.Gender,
            command.Notification,
            command.Email,
            command.Phone,
            command.Role,
            command.Status,
            model))

        self.AddDomainEvent(ExempleUpdateEvent(
            self.Id, command, model))

    def Delete(self):
        self.AddDomainEvent(ExempleDeleteDomainEvent(
            self.Id,
            self.FirstName,
            self.LastName,
            self.Gender,
            self.Notification,
            str(self.Email),
            str(self.Phone),
            self.Role))

        self.AddDomainEvent(ExempleDeleteEvent(
            self.Id,
            self.FirstName,
            self.LastName,
            self.Gender,
            self.Notification,
            str(self.Email),
            str(self.Phone),
            self.Role))
