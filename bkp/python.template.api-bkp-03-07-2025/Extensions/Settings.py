import os
from dotenv import load_dotenv

# Carrega o único .env da raiz
load_dotenv()


class Settings:
    # Informações da aplicação
    PROJECT_NAME = "API Exemple"
    VERSION = "v1"

    # SQL Server
    SQL_CONNECTION = os.getenv("SQL_CONNECTION")

    # Redis / Cache
    CACHE_CONNECTION = os.getenv("CACHE_CONNECTION")

    # MongoDB
    MONGO_URI = os.getenv("MONGO_URI")
    MONGO_DB = os.getenv("MONGO_DB")

    # JWT
    JWT_KEY = os.getenv("JWT_KEY", "changeme")
    JWT_ISSUER = os.getenv("JWT_ISSUER", "issuer-default")
    JWT_AUDIENCE = os.getenv("JWT_AUDIENCE", "audience-default")
    JWT_TIMEOUT = int(os.getenv("JWT_TIMEOUT", "28800"))
    JWT_ALGORITHM = "HS256"

    # RabbitMQ
    RABBIT_HOST = os.getenv("RABBIT_HOST")
    RABBIT_PORT = int(os.getenv("RABBIT_PORT", "5672"))
    RABBIT_USER = os.getenv("RABBIT_USER")
    RABBIT_PASS = os.getenv("RABBIT_PASS")
    RABBIT_QUEUE = os.getenv("RABBIT_QUEUE")

    # Kafka
    KAFKA_BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP")
    KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")
    KAFKA_GROUP = os.getenv("KAFKA_GROUP")

    # API Gateway - Auth
    API_AUTH_URL = os.getenv("API_AUTH_URL")
    API_AUTH_CLIENT_ID = os.getenv("API_AUTH_CLIENT_ID")
    API_AUTH_CLIENT_SECRET = os.getenv("API_AUTH_CLIENT_SECRET")


settings = Settings()
