from pydantic import BaseModel, EmailStr

class ForgotPasswordDto(BaseModel):
    Email: EmailStr
