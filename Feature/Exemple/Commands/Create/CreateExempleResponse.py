from uuid import UUID
from Common.Response.BaseResponse import BaseResponse


class CreateExempleResponse(BaseResponse):
    """
    Response class for the creation of an Exemple entity.
    """

    def __init__(self, Id: UUID):
        self.Id = Id
