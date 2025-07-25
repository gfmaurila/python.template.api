from fastapi import APIRouter
from application.Auth.dtos.AuthCommand import AuthCommand
from application.Auth.commands.AuthCommandHandler import AuthCommandHandler

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
async def Login(command: AuthCommand):
    handler = AuthCommandHandler()
    result = await handler.Handle(command)
    return result
