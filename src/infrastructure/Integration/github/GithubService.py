# src/infrastructure/integrations/github/GithubService.py

import requests
from core.Config import GetSettings
from domain.entities.GithubUserEntity import GithubUserEntity
from domain.entities.GithubRepoEntity import GithubRepoEntity


class GithubService:
    def __init__(self):
        settings = GetSettings()
        self._username = settings.GITHUB_USERNAME
        self._base_url = settings.GITHUB_API_URL
        self._token = settings.GITHUB_TOKEN

    def _get_headers(self):
        if self._token:
            return {"Authorization": f"token {self._token}"}
        return {}

    def GetUserProfile(self) -> GithubUserEntity:
        response = requests.get(f"{self._base_url}/users/{self._username}", headers=self._get_headers())
        response.raise_for_status()
        data = response.json()
        return GithubUserEntity(
            login=data["login"],
            name=data.get("name", ""),
            public_repos=data["public_repos"],
            followers=data["followers"],
            following=data["following"],
            html_url=data["html_url"]
        )

    def GetUserRepos(self) -> list[GithubRepoEntity]:
        response = requests.get(f"{self._base_url}/users/{self._username}/repos", headers=self._get_headers())
        response.raise_for_status()
        repos = response.json()
        return [
            GithubRepoEntity(
                name=repo["name"],
                html_url=repo["html_url"],
                description=repo.get("description", ""),
                language=repo.get("language", "")
            ) for repo in repos
        ]
