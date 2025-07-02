from Common.domain.ValueObjects.ValueObject import ValueObject


class Email(ValueObject):
    """
    Represents an email value object, ensuring consistency and immutability.
    """

    def __init__(self, Address: str):
        self.Address = Address.strip().lower()

    def __str__(self) -> str:
        return self.Address

    def GetEqualityComponents(self):
        yield self.Address
