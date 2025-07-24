# src/application/Message/commands/UpdateMessageCommand.py

from application.Message.dtos.MessageDto import MessageDto
from infrastructure.repositories.MessageRepository import MessageRepository
from domain.entities.MessageEntity import MessageEntity

class UpdateMessageCommand:
    def __init__(self, repository: MessageRepository):
        self._repository = repository

    def Handle(self, id: str, dto: MessageDto) -> None:
        entity = MessageEntity(Id=id, **dto.dict())
        self._repository.update(id, entity)
