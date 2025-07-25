from datetime import datetime, timedelta
from jose import jwt
import uuid
from core.Config import GetSettings

class AuthService:
    def __init__(self):
        self._settings = GetSettings()

    def GenerateAccessToken(self, userId: str, email: str, roles: list[str]) -> tuple[str, int]:
        expires_delta = timedelta(minutes=15)
        expire = datetime.utcnow() + expires_delta

        payload = {
            "sub": userId,
            "email": email,
            "roles": roles,
            "exp": expire,
            "iat": datetime.utcnow()
        }

        token = jwt.encode(
            payload,
            self._settings.SECRET_KEY,
            algorithm="HS256"
        )

        return token, int(expires_delta.total_seconds())

    def GenerateRefreshToken(self) -> str:
        return str(uuid.uuid4())
