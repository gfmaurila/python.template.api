from abc import ABC
from datetime import datetime
from uuid import UUID, uuid4
from typing import List, Optional, Iterable

from Common.domain.events.Event import Event
from Common.domain.IEntity import IEntityWithKey


class BaseEntity(IEntityWithKey[UUID], ABC):
    """
    Base class that represents an entity with common behaviors and properties.
    """

    def __init__(self):
        self.Id: UUID = uuid4()
        self.Status: bool = True
        self.DtInsert: Optional[datetime] = None
        self.DtInsertId: Optional[int] = None
        self.DtUpdate: Optional[datetime] = None
        self.DtUpdateId: Optional[int] = None
        self.DtDelete: Optional[datetime] = None
        self.DtDeleteId: Optional[int] = None
        self._domain_events: List[Event] = []

    def SetId(self, id: UUID):
        """
        Sets the entity's unique identifier.
        """
        self.Id = id

    @property
    def DomainEvents(self) -> Iterable[Event]:
        """
        Gets the list of domain events associated with the entity.
        """
        return self._domain_events.copy()

    def AddDomainEvent(self, domain_event: Event):
        """
        Adds a domain event to the entity's list of events.
        """
        self._domain_events.append(domain_event)

    def ClearDomainEvents(self):
        """
        Clears all domain events associated with the entity.
        """
        self._domain_events.clear()
