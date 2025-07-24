# src/domain/entities/MessageEntity.py

from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional

class MessageEntity(BaseModel):
    Id: Optional[str] = Field(default=None, alias="_id")
    Sender: str
    Recipient: str
    Content: str
    SentAt: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True
        allow_population_by_field_name = True
