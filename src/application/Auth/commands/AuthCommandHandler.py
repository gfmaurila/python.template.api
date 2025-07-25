from application.Auth.dtos.AuthCommand import AuthCommand
from application.Auth.dtos.AuthTokenResponse import AuthTokenResponse
from application.Auth.validators.AuthCommandValidator import AuthCommandValidator
from infrastructure.service.AuthService import AuthService
from infrastructure.repositories.UserRepository import UserRepository
from infrastructure.repositories.RefreshTokenRepository import RefreshTokenRepository
from domain.entities.User.events.UserLoggedInDomainEvent import UserLoggedInDomainEvent
from fastapi import HTTPException

class AuthCommandHandler:
    def __init__(self):
        self._validator = AuthCommandValidator()
        self._authService = AuthService()
        self._userRepository = UserRepository()
        self._refreshRepository = RefreshTokenRepository()

    async def Handle(self, command: AuthCommand) -> AuthTokenResponse:
        self._validator.Validate(command)

        user = await self._userRepository.GetAuthByEmailPassword(command.Email, command.Password)
        if user is None:
            raise HTTPException(status_code=400, detail="Usuário ou senha inválidos.")

        accessToken, expiresIn = self._authService.GenerateAccessToken(str(user.Id), user.Email.address, ["USER"])
        refreshToken = self._authService.GenerateRefreshToken()

        await self._refreshRepository.Save(str(user.Id), refreshToken)

        user.AddDomainEvent(UserLoggedInDomainEvent(str(user.Id), user.Email.address, accessToken))

        return AuthTokenResponse(
            AccessToken=accessToken,
            RefreshToken=refreshToken,
            ExpiresIn=expiresIn
        )
