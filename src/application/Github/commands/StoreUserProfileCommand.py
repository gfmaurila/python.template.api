# src/application/Github/commands/StoreUserProfileCommand.py

from application.Github.queries.GetUserProfileQuery import GetUserProfileQuery
from infrastructure.Integration.github.GithubService import GithubService
from infrastructure.repositories.GithubMongoRepository import GithubMongoRepository

class StoreUserProfileCommand:
    def __init__(self):
        self._service = GithubService()
        self._repository = GithubMongoRepository()

    def Handle(self):
        query = GetUserProfileQuery(self._service)
        profile = query.Handle()
        self._repository.ResetUserProfile(profile.__dict__)
