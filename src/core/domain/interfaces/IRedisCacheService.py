from abc import ABC, abstractmethod
from datetime import timedelta
from typing import Callable, Generic, List, Optional, TypeVar

T = TypeVar("T")

class IRedisCacheService(ABC, Generic[T]):
    @abstractmethod
    async def SetAsync(self, key: str, value: T, expiry: Optional[timedelta] = None) -> bool:
        pass

    @abstractmethod
    async def AddToListAsync(self, listKey: str, value: T) -> int:
        pass

    @abstractmethod
    async def GetOrCreateAsync(self, key: str, createItem: Callable[[], T], expiry: Optional[timedelta] = None) -> T:
        pass

    @abstractmethod
    async def GetListAsync(self, listKey: str) -> List[T]:
        pass

    @abstractmethod
    async def RemoveFromListAsync(self, listKey: str, value: T) -> int:
        pass

    @abstractmethod
    async def GetAsync(self, key: str) -> Optional[T]:
        pass

    @abstractmethod
    async def DeleteAsync(self, key: str) -> bool:
        pass

    @abstractmethod
    async def ClearDatabaseAsync(self) -> None:
        pass
