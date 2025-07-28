from domain.interfaces.IRegionMySqlRepository import IRegionMySqlRepository
from infrastructure.repositories.RegionMySqlRepository import RegionMySqlRepository

class GetAllRegionsMQuery:
    def __init__(self, repository: IRegionMySqlRepository = RegionMySqlRepository()):
        self._repository: IRegionMySqlRepository = repository

    def Handle(self):
        return self._repository.GetAll()
