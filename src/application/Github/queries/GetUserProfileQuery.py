# src/application/Github/queries/GetUserProfileQuery.py


from infrastructure.Integration.github.GithubService import GithubService


class GetUserProfileQuery:
    def __init__(self, service: GithubService):
        self._service = service

    def Handle(self):
        return self._service.GetUserProfile()
