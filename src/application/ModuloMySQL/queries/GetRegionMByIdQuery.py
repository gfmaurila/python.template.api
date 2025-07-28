from domain.interfaces.IRegionMySqlRepository import IRegionMySqlRepository
from infrastructure.repositories.RegionMySqlRepository import RegionMySqlRepository

class GetRegionMByIdQuery:
    def __init__(self, repository: IRegionMySqlRepository = RegionMySqlRepository()):
        self._repository: IRegionMySqlRepository = repository

    def Handle(self, regionId: int):
        return self._repository.GetById(regionId)
