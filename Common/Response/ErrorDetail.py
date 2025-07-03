from pydantic import BaseModel


class ErrorDetail(BaseModel):
    """
    Represents detailed information about an error in an API response.
    """

    Message: str

    def __init__(self, message: str):
        super().__init__(Message=message)
