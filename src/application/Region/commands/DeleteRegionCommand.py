from infrastructure.repositories.RegionOracleRepository import RegionOracleRepository

class DeleteRegionCommand:
    def __init__(self, repository: RegionOracleRepository):
        self._repository = repository

    def Handle(self, regionId: int) -> None:
        self._repository.Delete(regionId)
