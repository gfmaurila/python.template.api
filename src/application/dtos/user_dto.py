
# src/application/dtos/user_dto.py

from pydantic import BaseModel

class UserDTO(BaseModel):
    name: str
    email: str
