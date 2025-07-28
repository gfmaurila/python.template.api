from domain.interfaces.IRegionMySqlRepository import IRegionMySqlRepository
from infrastructure.repositories.RegionMySqlRepository import RegionMySqlRepository
from application.Region.dtos.RegionDto import RegionDto

class CreateRegionMCommand:
    def __init__(self, repository: IRegionMySqlRepository = RegionMySqlRepository()):
        self._repository: IRegionMySqlRepository = repository

    def Handle(self, dto: RegionDto) -> None:
        self._repository.Insert(dto)
