from domain.interfaces.IRegionOracleRepository import IRegionOracleRepository
from infrastructure.repositories.RegionOracleRepository import RegionOracleRepository

class DeleteRegionCommand:
    def __init__(self, repository: IRegionOracleRepository = RegionOracleRepository()):
        self._repository: IRegionOracleRepository = repository

    def Handle(self, regionId: int) -> None:
        self._repository.Delete(regionId)
