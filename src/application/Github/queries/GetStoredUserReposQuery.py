# src/application/Github/queries/GetStoredUserReposQuery.py

from infrastructure.repositories.GithubMongoRepository import GithubMongoRepository
from bson import ObjectId

class GetStoredUserReposQuery:
    def __init__(self):
        self._repository = GithubMongoRepository()

    def Handle(self) -> list[dict]:
        repos = self._repository.GetStoredUserRepos()
        for r in repos:
            if "_id" in r:
                r["_id"] = str(r["_id"])
        return repos

