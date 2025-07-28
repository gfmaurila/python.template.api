from application.Region.dtos.RegionDto import RegionDto
from domain.interfaces.IRegionOracleRepository import IRegionOracleRepository
from infrastructure.repositories.RegionOracleRepository import RegionOracleRepository

class UpdateRegionCommand:
    def __init__(self, repository: IRegionOracleRepository = RegionOracleRepository()):
        self._repository: IRegionOracleRepository = repository

    def Handle(self, dto: RegionDto) -> None:
        self._repository.Update(dto)
