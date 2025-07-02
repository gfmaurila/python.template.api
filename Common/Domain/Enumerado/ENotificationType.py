from enum import Enum


class ENotificationType(int, Enum):
    """
    Represents the types of notifications available.
    """
    SMS = 0
    Email = 1
    WhatsApp = 2

    @property
    def description(self) -> str:
        return {
            ENotificationType.SMS: "Notification via SMS",
            ENotificationType.Email: "Notification via email",
            ENotificationType.WhatsApp: "Notification via WhatsApp",
        }[self]
