# src/application/User/dtos/UserFilterDto.py

from pydantic import BaseModel
from typing import Optional


class UserFilterDto(BaseModel):
    Name: Optional[str] = None
    Email: Optional[str] = None
    Page: int = 1
    PageSize: int = 10

