from pydantic import BaseModel, EmailStr, Field

class AuthCommand(BaseModel):
    Email: EmailStr = Field(..., description="E-mail do usuário")
    Password: str = Field(..., min_length=6, description="Senha do usuário")
