# src/application/Github/commands/StoreUserReposCommand.py

from application.Github.queries.GetUserReposQuery import GetUserReposQuery
from infrastructure.Integration.github.GithubService import GithubService
from infrastructure.repositories.GithubMongoRepository import GithubMongoRepository

class StoreUserReposCommand:
    def __init__(self):
        self._service = GithubService()
        self._repository = GithubMongoRepository()

    def Handle(self):
        query = GetUserReposQuery(self._service)
        repos = query.Handle()
        self._repository.ResetUserRepos([repo.__dict__ for repo in repos])
