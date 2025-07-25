# src/domain/entities/GithubUserEntity.py

class GithubUserEntity:
    def __init__(self, login: str, name: str, public_repos: int, followers: int, following: int, html_url: str):
        self.Login = login
        self.Name = name
        self.PublicRepos = public_repos
        self.Followers = followers
        self.Following = following
        self.HtmlUrl = html_url
