import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME = "API Exemple"
    VERSION = "v1"
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "changeme")
    JWT_ALGORITHM = "HS256"
    JWT_ISSUER = os.getenv("JWT_ISSUER", "your-issuer")
    JWT_AUDIENCE = os.getenv("JWT_AUDIENCE", "your-audience")

settings = Settings()
