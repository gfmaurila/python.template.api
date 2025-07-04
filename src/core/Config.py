from pydantic import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    app_name: str = "Python Template API"
    environment: str = "development"
    debug: bool = True
    secret_key: str
    issuer: str
    audience: str

    class Config:
        env_file = ".env"  # será substituído dinamicamente no start

@lru_cache
def GetSettings():
    return Settings()
