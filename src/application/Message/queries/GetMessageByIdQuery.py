# src/application/Message/queries/GetMessageByIdQuery.py

from infrastructure.repositories.MessageRepository import MessageRepository

class GetMessageByIdQuery:
    def __init__(self, repository: MessageRepository):
        self._repository = repository

    def Handle(self, id: str):
        return self._repository.find_by_id(id)
