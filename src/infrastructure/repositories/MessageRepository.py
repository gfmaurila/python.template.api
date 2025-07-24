# src/infrastructure/repositories/MessageRepository.py

from pymongo import MongoClient
from bson import ObjectId
from core.Config import GetSettings
from domain.entities.MessageEntity import MessageEntity

class MessageRepository:
    def __init__(self):
        settings = GetSettings()
        client = MongoClient(settings.MONGO_LOG_CONN)
        self.collection = client[settings.MONGO_LOG_DB]["messages"]

    def insert(self, entity: MessageEntity):
        result = self.collection.insert_one(entity.model_dump(by_alias=True, exclude={"Id"}))
        return str(result.inserted_id)

    def find_all(self):
        return list(self.collection.find().sort("SentAt", -1))

    def find_by_id(self, id: str):
        return self.collection.find_one({"_id": ObjectId(id)})

    def update(self, id: str, entity: MessageEntity):
        self.collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": entity.model_dump(by_alias=True, exclude={"Id"})}
        )

    def delete(self, id: str):
        return self.collection.delete_one({"_id": ObjectId(id)}).deleted_count
