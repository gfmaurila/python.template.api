from abc import ABC
from datetime import datetime
from uuid import UUID
from typing import Optional


class INotification(ABC):
    """
    Marker interface for notification events (equivalente a MediatR.INotification)
    """
    pass


class Event(INotification, ABC):
    """
    Represents a base class for domain events.
    """

    MessageType: str
    AggregateId: UUID
    OccurredOn: datetime

    def __init__(self, message_type: str, aggregate_id: UUID):
        self.MessageType = message_type
        self.AggregateId = aggregate_id
        self.OccurredOn = datetime.utcnow()
