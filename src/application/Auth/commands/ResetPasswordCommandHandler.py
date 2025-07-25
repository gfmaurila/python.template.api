from application.Auth.dtos.ResetPasswordDto import ResetPasswordDto
from infrastructure.repositories.UserRepository import UserRepository
from infrastructure.service.ForgotPasswordCodeService import ForgotPasswordCodeService
from domain.entities.User.events.UserPasswordResetDomainEvent import UserPasswordResetDomainEvent
from core.util.Password import Password
from fastapi import HTTPException

class ResetPasswordCommandHandler:
    def __init__(self):
        self._repository = UserRepository()
        self._codeService = ForgotPasswordCodeService()

    async def Handle(self, dto: ResetPasswordDto):
        userId = await self._codeService.GetUserIdByCode(dto.Code)
        if not userId:
            raise HTTPException(status_code=400, detail="Código inválido ou expirado.")

        user = await self._repository.GetById(userId)
        if not user:
            raise HTTPException(status_code=404, detail="Usuário não encontrado.")

        user.Senha = Password.ComputeSha256Hash(dto.NewPassword)
        await self._repository.Update(userId, user)

        await self._codeService.DeleteCode(dto.Code)

        user.AddDomainEvent(UserPasswordResetDomainEvent(userId))
        return {"message": "Senha redefinida com sucesso."}