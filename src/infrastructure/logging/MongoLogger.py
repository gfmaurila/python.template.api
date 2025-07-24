# src/infrastructure/logging/MongoLogger.py

from loguru import logger
from pymongo import MongoClient
from datetime import datetime
from core.Config import GetSettings
import sys

class MongoDBHandler:
    def __init__(self, connection_string: str, database: str, collection: str):
        self.client = MongoClient(connection_string)
        self.collection = self.client[database][collection]

    def write(self, message):
        self.collection.insert_one({
            "timestamp": datetime.utcnow(),
            "message": message.strip()
        })

    def flush(self):
        pass

def ConfigureLogging():
    settings = GetSettings()

    logger.remove()  # Remove log padrão

    # Console
    logger.add(sys.stdout, level="DEBUG", enqueue=True)

    # MongoDB
    mongo_handler = MongoDBHandler(
        connection_string=settings.MONGO_LOG_CONN,
        database=settings.MONGO_LOG_DB,
        collection=settings.MONGO_LOG_COLLECTION
    )
    logger.add(mongo_handler, level="DEBUG", enqueue=True)

    logger.debug("Log MongoDB configurado via .env")
