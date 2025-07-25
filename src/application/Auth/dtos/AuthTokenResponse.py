from pydantic import BaseModel

class AuthTokenResponse(BaseModel):
    AccessToken: str
    RefreshToken: str
    ExpiresIn: int
