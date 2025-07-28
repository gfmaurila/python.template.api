from domain.interfaces.IRegionOracleRepository import IRegionOracleRepository
from infrastructure.repositories.RegionOracleRepository import RegionOracleRepository

class GetAllRegionsQuery:
    def __init__(self, repository: IRegionOracleRepository = RegionOracleRepository()):
        self._repository: IRegionOracleRepository = repository

    def Handle(self):
        return self._repository.GetAll()
