from infrastructure.repositories.RegionOracleRepository import RegionOracleRepository

class GetAllRegionsQuery:
    def __init__(self, repository: RegionOracleRepository):
        self._repository = repository

    def Handle(self):
        return self._repository.GetAll()
