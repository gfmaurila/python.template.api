from abc import ABC
from typing import Generic, TypeVar

TKey = TypeVar("TKey")


class IEntity(ABC):
    """
    Marker interface to represent an entity.
    """
    pass


class IEntityWithKey(IEntity, Generic[TKey]):
    """
    Marker interface to represent an entity with a strongly-typed key.
    """

    @property
    def Id(self) -> TKey:
        raise NotImplementedError("Id property must be implemented")
