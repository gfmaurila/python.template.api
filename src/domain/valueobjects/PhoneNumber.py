from typing import Iterable
from domain.valueobjects.ValueObject import ValueObject  # ajuste o caminho conforme sua estrutura


class PhoneNumber(ValueObject):
    """
    Represents a phone number as a value object, ensuring consistency and immutability.
    """

    def __init__(self, phone: str):
        """
        Initializes a new instance of the PhoneNumber class with the specified phone number.
        """
        if not isinstance(phone, str) or not phone.strip():
            raise ValueError("Invalid phone number")
        self._phone = phone.strip().lower()

    @property
    def phone(self) -> str:
        """
        Gets the phone number.
        """
        return self._phone

    def __str__(self) -> str:
        """
        Returns the phone number as a string.
        """
        return self._phone

    def get_equality_components(self) -> Iterable[str]:
        """
        Provides components for equality comparison.
        """
        yield self._phone
