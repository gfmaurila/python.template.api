from infrastructure.database.MySqlDatabase import GetMySqlConnection
from application.Region.dtos.RegionDto import RegionDto
from domain.interfaces.IRegionMySqlRepository import IRegionMySqlRepository
from typing import List, Optional

class RegionMySqlRepository(IRegionMySqlRepository):
    def GetAll(self) -> List[RegionDto]:
        with GetMySqlConnection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT RegionId, RegionName FROM Regions")
                rows = cursor.fetchall()
                return [RegionDto(RegionId=row["RegionId"], RegionName=row["RegionName"]) for row in rows]

    def GetById(self, regionId: int) -> Optional[RegionDto]:
        with GetMySqlConnection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT RegionId, RegionName FROM Regions WHERE RegionId = %s", (regionId,))
                row = cursor.fetchone()
                return RegionDto(RegionId=row["RegionId"], RegionName=row["RegionName"]) if row else None

    def Insert(self, dto: RegionDto) -> None:
        with GetMySqlConnection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO Regions (RegionId, RegionName) VALUES (%s, %s)",
                    (dto.RegionId, dto.RegionName)
                )

    def Update(self, dto: RegionDto) -> None:
        with GetMySqlConnection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "UPDATE Regions SET RegionName = %s WHERE RegionId = %s",
                    (dto.RegionName, dto.RegionId)
                )

    def Delete(self, regionId: int) -> None:
        with GetMySqlConnection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM Regions WHERE RegionId = %s", (regionId,))
