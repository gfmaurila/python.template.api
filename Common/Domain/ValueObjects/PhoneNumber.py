from Common.domain.ValueObjects.ValueObject import ValueObject


class PhoneNumber(ValueObject):
    """
    Represents a phone number as a value object, ensuring consistency and immutability.
    """

    def __init__(self, Phone: str):
        self.Phone = Phone.strip().lower()

    def __str__(self) -> str:
        return self.Phone

    def GetEqualityComponents(self):
        yield self.Phone
