# src/application/Message/commands/CreateMessageCommand.py

from domain.entities.MessageEntity import MessageEntity
from application.Message.dtos.MessageDto import MessageDto
from infrastructure.repositories.MessageRepository import MessageRepository

class CreateMessageCommand:
    def __init__(self, repository: MessageRepository):
        self._repository = repository

    def Handle(self, dto: MessageDto) -> str:
        entity = MessageEntity(**dto.dict())
        return self._repository.insert(entity)
