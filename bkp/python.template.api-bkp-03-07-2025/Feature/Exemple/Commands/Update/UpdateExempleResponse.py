from uuid import UUID
from Common.Response.BaseResponse import BaseResponse


class UpdateExempleResponse(BaseResponse):
    """
    Represents the response after updating an Exemple entity.
    """

    def __init__(self, Id: UUID):
        self.Id = Id
