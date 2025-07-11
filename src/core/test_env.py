# src/test_env.py

from core.Config import Settings

settings = Settings(_env_file="core/env/.env.development")

print("RABBITMQ_EXCHANGE =", settings.RABBITMQ_EXCHANGE)
print("APP_NAME =", settings.APP_NAME)
print("SECRET_KEY =", settings.SECRET_KEY)
