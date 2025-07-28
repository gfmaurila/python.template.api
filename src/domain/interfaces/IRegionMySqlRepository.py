from abc import ABC, abstractmethod
from application.Region.dtos.RegionDto import RegionDto
from typing import List, Optional

class IRegionMySqlRepository(ABC):

    @abstractmethod
    def GetAll(self) -> List[RegionDto]:
        pass

    @abstractmethod
    def GetById(self, regionId: int) -> Optional[RegionDto]:
        pass

    @abstractmethod
    def Insert(self, dto: RegionDto) -> None:
        pass

    @abstractmethod
    def Update(self, dto: RegionDto) -> None:
        pass

    @abstractmethod
    def Delete(self, regionId: int) -> None:
        pass
