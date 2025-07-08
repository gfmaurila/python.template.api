# src/core/domain/entities/BaseEntity.py

from datetime import datetime
from core.domain.events.Event import Event

class BaseEntity:
    def __init__(self):
        self.Id = None
        self.Status = True
        self.DtInsert = None
        self.DtUpdate = None
        self._domainEvents = []

    def SetId(self, id_):
        self.Id = id_

    def AddDomainEvent(self, domainEvent: Event):
        self._domainEvents.append(domainEvent)

    def ClearDomainEvents(self):
        self._domainEvents.clear()

    @property
    def DomainEvents(self):
        return self._domainEvents
