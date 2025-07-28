from application.Region.dtos.RegionDto import RegionDto
from infrastructure.repositories.RegionOracleRepository import RegionOracleRepository

class UpdateRegionCommand:
    def __init__(self, repository: RegionOracleRepository):
        self._repository = repository

    def Handle(self, dto: RegionDto) -> None:
        self._repository.Update(dto)

