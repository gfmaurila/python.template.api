# src/application/dtos/UserDto.py

from pydantic import BaseModel
from domain.enums.ENotificationType import ENotificationType
from domain.enums.EGender import EGender

class UserDto(BaseModel):
    Name: str
    Email: str
    Senha: str
    Phone: str
    Notification: ENotificationType
    Gender: EGender