from pydantic import BaseModel

class RegionDto(BaseModel):
    RegionId: int
    RegionName: str
