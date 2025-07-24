# src/application/Message/queries/GetAllMessagesQuery.py

from infrastructure.repositories.MessageRepository import MessageRepository

class GetAllMessagesQuery:
    def __init__(self, repository: MessageRepository):
        self._repository = repository

    def Handle(self):
        return self._repository.find_all()
