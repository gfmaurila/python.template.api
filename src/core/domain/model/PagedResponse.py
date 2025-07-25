# src/core/domain/model/PagedResponse.py

from typing import Generic, List, TypeVar
from pydantic import BaseModel

T = TypeVar("T")

class PagedResponse(BaseModel, Generic[T]):
    TotalItems: int
    PageSize: int
    CurrentPage: int
    TotalPages: int
    Items: List[T]
