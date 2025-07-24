# src/infrastructure/repositories/LogRepository.py

from pymongo import MongoClient
from core.Config import GetSettings

class LogRepository:
    def __init__(self):
        settings = GetSettings()
        client = MongoClient(settings.MONGO_LOG_CONN)
        self.collection = client[settings.MONGO_LOG_DB][settings.MONGO_LOG_COLLECTION]

    def get_all(self, limit: int = 1000):
        return list(self.collection.find().sort("timestamp", -1).limit(limit))

    def delete_all(self):
        result = self.collection.delete_many({})
        return result.deleted_count

    def delete_older_than(self, iso_date: str):
        from datetime import datetime
        date = datetime.fromisoformat(iso_date)
        result = self.collection.delete_many({"timestamp": {"$lt": date}})
        return result.deleted_count
