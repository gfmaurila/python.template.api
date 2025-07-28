from fastapi import APIRouter, HTTPException
from typing import List
from infrastructure.repositories.RegionOracleRepository import RegionOracleRepository
from application.Region.dtos.RegionDto import RegionDto
from application.Region.commands.CreateRegionCommand import CreateRegionCommand
from application.Region.commands.UpdateRegionCommand import UpdateRegionCommand
from application.Region.commands.DeleteRegionCommand import DeleteRegionCommand
from application.Region.queries.GetAllRegionsQuery import GetAllRegionsQuery
from application.Region.queries.GetRegionByIdQuery import GetRegionByIdQuery

router = APIRouter(prefix="/regions", tags=["Regions"])
repository = RegionOracleRepository()

@router.get("/", response_model=List[RegionDto])
def GetAll():
    return GetAllRegionsQuery(repository).Handle()

@router.get("/{id}", response_model=RegionDto)
def GetById(id: int):
    region = GetRegionByIdQuery(repository).Handle(id)
    if not region:
        raise HTTPException(status_code=404, detail="Region not found")
    return region

@router.post("/", response_model=str)
def Create(dto: RegionDto):
    CreateRegionCommand(repository).Handle(dto)
    return "Region created successfully"

@router.put("/", response_model=str)
def Update(dto: RegionDto):
    UpdateRegionCommand(repository).Handle(dto)
    return "Region updated successfully"

@router.delete("/{id}", response_model=str)
def Delete(id: int):
    DeleteRegionCommand(repository).Handle(id)
    return "Region deleted successfully"
