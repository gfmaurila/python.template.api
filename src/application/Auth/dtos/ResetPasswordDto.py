from pydantic import BaseModel, Field

class ResetPasswordDto(BaseModel):
    Code: str = Field(..., description="Código de redefinição")
    NewPassword: str = Field(..., min_length=6, description="Nova senha")