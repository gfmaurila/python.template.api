from typing import Generic, TypeVar, List, Optional
from pydantic import BaseModel
from Common.Response.ErrorDetail import ErrorDetail

T = TypeVar("T")


class ApiResult(BaseModel, Generic[T]):
    """
    Represents a standardized API response that includes the status,
    messages, errors, and data.
    """

    Success: bool
    SuccessMessage: Optional[str] = None
    StatusCode: int
    Errors: Optional[List[ErrorDetail]] = []
    Data: Optional[T] = None

    @staticmethod
    def CreateError(errors: List[ErrorDetail], status_code: int) -> "ApiResult":
        return ApiResult(
            Success=False,
            StatusCode=status_code,
            Errors=errors
        )

    @staticmethod
    def CreateSuccess(result: T) -> "ApiResult[T]":
        return ApiResult(
            Success=True,
            SuccessMessage="Created successfully!",
            StatusCode=200,
            Errors=[],
            Data=result
        )

    @staticmethod
    def CreateSuccessWithMessage(result: T, success_message: str) -> "ApiResult[T]":
        return ApiResult(
            Success=True,
            SuccessMessage=success_message,
            StatusCode=200,
            Errors=[],
            Data=result
        )
