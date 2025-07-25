# src/domain/entities/GithubRepoEntity.py

class GithubRepoEntity:
    def __init__(self, name: str, html_url: str, description: str, language: str):
        self.Name = name
        self.HtmlUrl = html_url
        self.Description = description
        self.Language = language
