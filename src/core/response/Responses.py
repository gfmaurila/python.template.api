from typing import Generic, List, Optional, TypeVar
from pydantic import BaseModel
from pydantic.generics import GenericModel

T = TypeVar("T")


class ErrorDetail(BaseModel):
    """
    Representa uma informação de erro detalhada.
    """
    message: str


class ApiResult(GenericModel, Generic[T]):
    """
    Representa uma resposta padronizada da API.
    """
    success: bool
    success_message: Optional[str] = None
    status_code: int
    errors: List[ErrorDetail] = []
    data: Optional[T] = None

    @classmethod
    def create_error(cls, errors: List[ErrorDetail], status_code: int = 400) -> "ApiResult":
        return cls(
            success=False,
            status_code=status_code,
            errors=errors
        )

    @classmethod
    def create_success(cls, data: Optional[T] = None, message: str = "Criado com sucesso!") -> "ApiResult":
        return cls(
            success=True,
            success_message=message,
            status_code=200,
            errors=[],
            data=data
        )
