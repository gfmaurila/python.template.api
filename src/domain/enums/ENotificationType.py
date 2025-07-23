# src/domain/enums/ENotificationType.py

from enum import IntEnum

class ENotificationType(IntEnum):
    """
    Represents the types of notifications available.
    """

    SMS = 0
    Email = 1
    WhatsApp = 2

    def description(self) -> str:
        descriptions = {
            ENotificationType.SMS: "Notification via SMS",
            ENotificationType.Email: "Notification via email",
            ENotificationType.WhatsApp: "Notification via WhatsApp",
        }
        return descriptions.get(self, "Unknown")

    def __str__(self):
        return self.description()

