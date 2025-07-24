# src/application/Log/commands/DeleteLogsCommand.py

from infrastructure.repositories.LogRepository import LogRepository

class DeleteLogsCommand:
    def __init__(self):
        self.repository = LogRepository()

    def delete_all(self):
        return self.repository.delete_all()

    def delete_older_than(self, iso_date: str):
        return self.repository.delete_older_than(iso_date)
