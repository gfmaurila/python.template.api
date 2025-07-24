# src/application/Message/dtos/MessageDto.py

from pydantic import BaseModel

class MessageDto(BaseModel):
    Sender: str
    Recipient: str
    Content: str
