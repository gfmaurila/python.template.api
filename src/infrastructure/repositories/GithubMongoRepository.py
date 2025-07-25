# src/infrastructure/repositories/GithubMongoRepository.py

from pymongo import MongoClient
from core.Config import GetSettings

class GithubMongoRepository:
    def __init__(self):
        settings = GetSettings()
        self._client = MongoClient(settings.MONGO_LOG_CONN)
        self._db = self._client[settings.MONGO_LOG_DB]

    def ResetUserProfile(self, profile: dict):
        collection = self._db["github_user_profile"]
        collection.delete_many({})
        collection.insert_one(profile)

    def ResetUserRepos(self, repos: list[dict]):
        collection = self._db["github_user_repos"]
        collection.delete_many({})
        if repos:
            collection.insert_many(repos)

    def GetStoredUserProfile(self) -> dict | None:
        return self._db["github_user_profile"].find_one()

    def GetStoredUserRepos(self) -> list[dict]:
        return list(self._db["github_user_repos"].find())

