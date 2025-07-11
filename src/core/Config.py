from pydantic_settings import BaseSettings
from functools import lru_cache
from dotenv import load_dotenv
from pydantic import Field
import os

# Define o ambiente (padrão: development)
ENVIRONMENT = os.getenv("ENVIRONMENT", "development").lower()

# Mapeia o arquivo .env conforme o ambiente
ENV_MAP = {
    "development": "src/core/env/.env.development",
    "docker": "src/core/env/.env.docker",
    "homolog": "src/core/env/.env.homolog",
    "production": "src/core/env/.env.production"
}

# Força o carregamento do .env correspondente
load_dotenv(dotenv_path=ENV_MAP.get(ENVIRONMENT, "src/core/env/.env.development"))

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
    REDIS_PASSWORD: str = Field(default=None, alias="REDIS_PASSWORD")

    class Config:
        populate_by_name = True  # necessário para acessar por atributo normal (REDIS_HOST)

@lru_cache
def GetSettings():
    return Settings(_env_file=ENV_MAP.get(ENVIRONMENT, "src/core/env/.env.development"))
