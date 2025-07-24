# src/application/Message/commands/DeleteMessageCommand.py

from infrastructure.repositories.MessageRepository import MessageRepository

class DeleteMessageCommand:
    def __init__(self, repository: MessageRepository):
        self._repository = repository

    def Handle(self, id: str) -> int:
        return self._repository.delete(id)
