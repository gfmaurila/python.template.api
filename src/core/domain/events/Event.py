# src/domain/events/Event.py

from uuid import uuid4
from datetime import datetime

class Event:
    def __init__(self):
        self.MessageType = self.__class__.__name__
        self.AggregateId = uuid4()
        self.OccurredOn = datetime.utcnow()
