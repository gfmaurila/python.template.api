# src/application/Github/queries/GetUserReposQuery.py

from infrastructure.Integration.github.GithubService import GithubService

class GetUserReposQuery:
    def __init__(self, service: GithubService):
        self._service = service

    def Handle(self):
        return self._service.GetUserRepos()
