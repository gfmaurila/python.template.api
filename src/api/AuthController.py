from fastapi import APIRouter
from application.Auth.dtos.AuthCommand import AuthCommand
from application.Auth.commands.AuthCommandHandler import AuthCommandHandler

from application.Auth.commands.ForgotPasswordCommandHandler import ForgotPasswordCommandHandler
from application.Auth.commands.ResetPasswordCommandHandler import ResetPasswordCommandHandler
from application.Auth.dtos.ForgotPasswordDto import ForgotPasswordDto
from application.Auth.dtos.ResetPasswordDto import ResetPasswordDto

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
async def Login(command: AuthCommand):
    handler = AuthCommandHandler()
    result = await handler.Handle(command)
    return result

@router.post("/forgot-password")
async def ForgotPassword(dto: ForgotPasswordDto):
    handler = ForgotPasswordCommandHandler()
    return await handler.Handle(dto)

@router.post("/reset-password")
async def ResetPassword(dto: ResetPasswordDto):
    handler = ResetPasswordCommandHandler()
    return await handler.Handle(dto)
