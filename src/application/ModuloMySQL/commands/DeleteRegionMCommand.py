from domain.interfaces.IRegionMySqlRepository import IRegionMySqlRepository
from infrastructure.repositories.RegionMySqlRepository import RegionMySqlRepository

class DeleteRegionMCommand:
    def __init__(self, repository: IRegionMySqlRepository = RegionMySqlRepository()):
        self._repository: IRegionMySqlRepository = repository

    def Handle(self, regionId: int) -> None:
        self._repository.Delete(regionId)
