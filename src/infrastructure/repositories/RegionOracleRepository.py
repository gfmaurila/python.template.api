from infrastructure.database.OracleDatabase import GetOracleConnection
from application.Region.dtos.RegionDto import RegionDto
from domain.interfaces.IRegionOracleRepository import IRegionOracleRepository
from typing import List, Optional

class RegionOracleRepository(IRegionOracleRepository):
    def GetAll(self) -> List[RegionDto]:
        with GetOracleConnection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT REGION_ID, REGION_NAME FROM HR.REGIONS")
                return [RegionDto(RegionId=row[0], RegionName=row[1]) for row in cursor]

    def GetById(self, regionId: int) -> Optional[RegionDto]:
        with GetOracleConnection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT REGION_ID, REGION_NAME FROM HR.REGIONS WHERE REGION_ID = :id", [regionId])
                row = cursor.fetchone()
                return RegionDto(RegionId=row[0], RegionName=row[1]) if row else None

    def Insert(self, dto: RegionDto) -> None:
        with GetOracleConnection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO HR.REGIONS (REGION_ID, REGION_NAME) VALUES (:1, :2)",
                    [dto.RegionId, dto.RegionName]
                )
                conn.commit()

    def Update(self, dto: RegionDto) -> None:
        with GetOracleConnection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "UPDATE HR.REGIONS SET REGION_NAME = :1 WHERE REGION_ID = :2",
                    [dto.RegionName, dto.RegionId]
                )
                conn.commit()

    def Delete(self, regionId: int) -> None:
        with GetOracleConnection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM HR.REGIONS WHERE REGION_ID = :1", [regionId])
                conn.commit()
