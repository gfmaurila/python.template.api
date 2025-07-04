from typing import Iterable
from domain.valueobjects.ValueObject import ValueObject  # ajuste o caminho conforme necessário


class Email(ValueObject):
    """
    Represents an email value object, ensuring consistency and immutability.
    """

    def __init__(self, address: str):
        """
        Initializes a new instance of the Email class with the specified email address.
        """
        if not isinstance(address, str) or "@" not in address:
            raise ValueError("Invalid email address")
        self._address = address.strip().lower()

    @property
    def address(self) -> str:
        """
        Gets the email address.
        """
        return self._address

    def __str__(self) -> str:
        """
        Returns the email address as a string.
        """
        return self._address

    def get_equality_components(self) -> Iterable[str]:
        """
        Provides components for equality comparison.
        """
        yield self._address
