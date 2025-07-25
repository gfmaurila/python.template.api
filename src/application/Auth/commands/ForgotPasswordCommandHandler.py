from application.Auth.dtos.ForgotPasswordDto import ForgotPasswordDto
from infrastructure.repositories.UserRepository import UserRepository
from infrastructure.service.ForgotPasswordCodeService import ForgotPasswordCodeService
from infrastructure.service.EmailService import EmailService
from domain.entities.User.events.UserForgotPasswordDomainEvent import UserForgotPasswordDomainEvent
from fastapi import HTTPException

class ForgotPasswordCommandHandler:
    def __init__(self):
        self._repository = UserRepository()
        self._codeService = ForgotPasswordCodeService()
        self._emailService = EmailService()

    async def Handle(self, dto: ForgotPasswordDto):
        user = await self._repository.GetByEmail(dto.Email)
        if not user:
            raise HTTPException(status_code=404, detail="Usuário não encontrado.")

        code = await self._codeService.GenerateCode(user.Id)
        self._emailService.SendResetPasswordEmail(dto.Email, code)

        user.AddDomainEvent(UserForgotPasswordDomainEvent(dto.Email, code))
        return {"message": "Link de redefinição enviado para o e-mail."}