from fastapi import APIRouter, HTTPException, Response
from typing import List
from application.Region.dtos.RegionDto import RegionDto
from application.ModuloMySQL.commands.CreateRegionMCommand import CreateRegionMCommand
from application.ModuloMySQL.commands.UpdateRegionMCommand import UpdateRegionMCommand
from application.ModuloMySQL.commands.DeleteRegionMCommand import DeleteRegionMCommand
from application.ModuloMySQL.queries.GetAllRegionsMQuery import GetAllRegionsMQuery
from application.ModuloMySQL.queries.GetRegionMByIdQuery import GetRegionMByIdQuery

router = APIRouter(prefix="/regionsMySQL", tags=["Regions MySQL"])

@router.get("/", response_model=List[RegionDto])
def GetAll():
    query = GetAllRegionsMQuery()
    return query.Handle()

@router.get("/{regionId}", response_model=RegionDto)
def GetById(regionId: int):
    query = GetRegionMByIdQuery()
    result = query.Handle(regionId)
    if not result:
        raise HTTPException(status_code=404, detail="Region not found")
    return result

@router.post("/", status_code=201)
def Create(dto: RegionDto):
    command = CreateRegionMCommand()
    command.Handle(dto)
    return {"message": "Region created successfully."}

@router.put("/", status_code=204)
def Update(dto: RegionDto):
    command = UpdateRegionMCommand()
    command.Handle(dto)
    return Response(status_code=204)

@router.delete("/{regionId}", status_code=204)
def Delete(regionId: int):
    command = DeleteRegionMCommand()
    command.Handle(regionId)
    return Response(status_code=204)
