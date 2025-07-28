from infrastructure.repositories.RegionOracleRepository import RegionOracleRepository

class GetRegionByIdQuery:
    def __init__(self, repository: RegionOracleRepository):
        self._repository = repository

    def Handle(self, regionId: int):
        return self._repository.GetById(regionId)
