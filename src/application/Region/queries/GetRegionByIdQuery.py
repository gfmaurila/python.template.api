from domain.interfaces.IRegionOracleRepository import IRegionOracleRepository
from infrastructure.repositories.RegionOracleRepository import RegionOracleRepository

class GetRegionByIdQuery:
    def __init__(self, repository: IRegionOracleRepository = RegionOracleRepository()):
        self._repository: IRegionOracleRepository = repository

    def Handle(self, regionId: int):
        return self._repository.GetById(regionId)
