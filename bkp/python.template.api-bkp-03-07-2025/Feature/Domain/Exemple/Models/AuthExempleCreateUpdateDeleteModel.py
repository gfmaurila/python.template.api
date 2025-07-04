from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class AuthExempleCreateUpdateDeleteModel(BaseModel):
    """
    Represents audit information for create, update, and delete actions.
    """

    DtInsert: Optional[datetime]
    DtInsertId: Optional[int]
    DtUpdate: Optional[datetime]
    DtUpdateId: Optional[int]
    DtDelete: Optional[datetime]
    DtDeleteId: Optional[int]
