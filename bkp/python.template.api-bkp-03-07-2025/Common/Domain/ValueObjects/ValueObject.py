from abc import ABC, abstractmethod
from typing import Any, Iterable


class ValueObject(ABC):
    """
    Represents a base class for implementing value objects.
    Provides methods for equality comparison based on the object's components.
    """

    @abstractmethod
    def GetEqualityComponents(self) -> Iterable[Any]:
        """
        Derived classes must implement this method to specify the relevant components.
        """
        pass

    def __eq__(self, other: Any) -> bool:
        if other is None or type(other) != type(self):
            return False

        return list(self.GetEqualityComponents()) == list(other.GetEqualityComponents())

    def __ne__(self, other: Any) -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        return hash(tuple(self.GetEqualityComponents()))

    @staticmethod
    def EqualOperator(left: 'ValueObject', right: 'ValueObject') -> bool:
        if (left is None) != (right is None):
            return False
        return left == right

    @staticmethod
    def NotEqualOperator(left: 'ValueObject', right: 'ValueObject') -> bool:
        return not ValueObject.EqualOperator(left, right)
