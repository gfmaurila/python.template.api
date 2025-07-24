from pydantic_settings import BaseSettings
from functools import lru_cache
from dotenv import load_dotenv
from pydantic import Field
import os
import pathlib

from pydantic import BaseModel
from functools import lru_cache

# Base path absoluto
BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

# Define o ambiente (padrão: development)
ENVIRONMENT = os.getenv("ENVIRONMENT", "development").lower()

# Mapeia o arquivo .env conforme o ambiente
ENV_MAP = {
    "development": BASE_DIR / "core/env/.env.development",
    "docker": BASE_DIR / "core/env/.env.docker",
    "homolog": BASE_DIR / "core/env/.env.homolog",
    "production": BASE_DIR / "core/env/.env.production"
}

# Força o carregamento do .env correspondente
load_dotenv(dotenv_path=str(ENV_MAP.get(ENVIRONMENT, BASE_DIR / "core/env/.env.development")))

class Settings(BaseSettings):
    APP_NAME: str = Field(..., alias="APP_NAME")
    ENVIRONMENT: str = Field(default=ENVIRONMENT, alias="ENVIRONMENT")
    DEBUG: bool = Field(default=True, alias="DEBUG")

    SECRET_KEY: str = Field(..., alias="SECRET_KEY")
    ISSUER: str = Field(..., alias="ISSUER")
    AUDIENCE: str = Field(..., alias="AUDIENCE")

    REDIS_HOST: str = Field(default="localhost", alias="REDIS_HOST")
    REDIS_PORT: int = Field(default=6379, alias="REDIS_PORT")
    REDIS_DB: int = Field(default=0, alias="REDIS_DB")
    REDIS_DB_USER: int = Field(default=1, alias="REDIS_DB_USER")
    REDIS_DB_USER_DELETE: int = Field(default=2, alias="REDIS_DB_USER_DELETE")
    REDIS_PASSWORD: str = Field(default="", alias="REDIS_PASSWORD")

    RABBITMQ_HOST: str = Field(default="localhost", alias="RABBITMQ_HOST")
    RABBITMQ_PORT: int = Field(default=5672, alias="RABBITMQ_PORT")
    RABBITMQ_USER: str = Field(default="guest", alias="RABBITMQ_USER")
    RABBITMQ_PASSWORD: str = Field(default="guest", alias="RABBITMQ_PASSWORD")

    RABBITMQ_EXCHANGE: str = Field(default="user-exchange", alias="RABBITMQ_EXCHANGE")
    RABBITMQ_QUEUE: str = Field(default="user-created-queue", alias="RABBITMQ_QUEUE")
    RABBITMQ_EXCHANGE_USER: str = Field(default="user-exchange", alias="RABBITMQ_EXCHANGE_USER")
    RABBITMQ_QUEUE_USER: str = Field(default="user-created-queue", alias="RABBITMQ_QUEUE_USER")
    RABBITMQ_EXCHANGE_PERSON: str = Field(default="person-exchange", alias="RABBITMQ_EXCHANGE_PERSON")
    RABBITMQ_QUEUE_PERSON: str = Field(default="person-created-queue", alias="RABBITMQ_QUEUE_PERSON")

    KAFKA_BOOTSTRAP_SERVERS: str = Field(default="localhost:9092", alias="KAFKA_BOOTSTRAP_SERVERS")
    KAFKA_TOPIC: str = Field(default="user-topic", alias="KAFKA_TOPIC")
    KAFKA_GROUP_ID: str = Field(default="user-group", alias="KAFKA_GROUP_ID")

    # SQL Server
    SQLSERVER_HOST: str = Field(..., alias="SQLSERVER_HOST")
    SQLSERVER_PORT: int = Field(..., alias="SQLSERVER_PORT")
    SQLSERVER_DB: str = Field(..., alias="SQLSERVER_DB")
    SQLSERVER_USER: str = Field(..., alias="SQLSERVER_USER")
    SQLSERVER_PASSWORD: str = Field(..., alias="SQLSERVER_PASSWORD")

    MONGO_LOG_CONN: str = Field(..., alias="MONGO_LOG_CONN")
    MONGO_LOG_DB: str = Field(..., alias="MONGO_LOG_DB")
    MONGO_LOG_COLLECTION: str = Field(..., alias="MONGO_LOG_COLLECTION")

    class Config:
        populate_by_name = True
        extra = "forbid"

@lru_cache()
def GetSettings():
    return Settings()

