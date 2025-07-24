# src/application/Log/queries/GetAllLogsQuery.py

from infrastructure.repositories.LogRepository import LogRepository

class GetAllLogsQuery:
    def __init__(self):
        self.repository = LogRepository()

    def execute(self, limit: int = 1000):
        return self.repository.get_all(limit)
