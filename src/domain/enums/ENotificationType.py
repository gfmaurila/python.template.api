from enum import Enum

class ENotificationType(Enum):
    """
    Represents the types of notifications available.
    """

    SMS = (0, "Notification via SMS")
    Email = (1, "Notification via email")
    WhatsApp = (2, "Notification via WhatsApp")

    def __init__(self, value: int, description: str):
        self._value_ = value
        self.description = description

    def __str__(self):
        return self.description
