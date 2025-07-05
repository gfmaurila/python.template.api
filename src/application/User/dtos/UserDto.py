
# src/application/dtos/UserDto.py

from pydantic import BaseModel

class UserDto(BaseModel):
    Name: str
    Email: str
