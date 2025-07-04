from abc import ABC, abstractmethod
from typing import Iterable, Any


class ValueObject(ABC):
    """
    Represents a base class for implementing value objects.
    Provides methods for equality comparison based on the object's components.
    """

    @abstractmethod
    def get_equality_components(self) -> Iterable[Any]:
        """
        Provides the components that define the equality of the value object.
        Derived classes must implement this method to specify the relevant components.
        """
        pass

    def __eq__(self, other: Any) -> bool:
        """
        Compares this value object with another object for equality.
        """
        if other is None or not isinstance(other, self.__class__):
            return False
        return all(a == b for a, b in zip(self.get_equality_components(), other.get_equality_components()))

    def __ne__(self, other: Any) -> bool:
        """
        Compares two value objects for inequality.
        """
        return not self.__eq__(other)

    def __hash__(self) -> int:
        """
        Generates a hash code for the value object based on its equality components.
        """
        return hash(tuple(self.get_equality_components()))
