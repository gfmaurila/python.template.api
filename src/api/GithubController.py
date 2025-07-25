# src/api/GithubController.py

from fastapi import APIRouter
from loguru import logger

from application.Github.commands.StoreUserProfileCommand import StoreUserProfileCommand
from application.Github.commands.StoreUserReposCommand import StoreUserReposCommand 
from infrastructure.Integration.github.GithubService import GithubService
from application.Github.queries.GetUserProfileQuery import GetUserProfileQuery
from application.Github.queries.GetUserReposQuery import GetUserReposQuery
from application.Github.queries.GetStoredUserProfileQuery import GetStoredUserProfileQuery
from application.Github.queries.GetStoredUserReposQuery import GetStoredUserReposQuery

router = APIRouter(prefix="/github", tags=["GitHub"])
service = GithubService()

@router.get("/user")
def GetUserProfile():
    logger.info("Buscando dados do usuário GitHub via API pública.")
    query = GetUserProfileQuery(service)
    return query.Handle()

@router.get("/repos")
def GetUserRepos():
    logger.info("Buscando repositórios do usuário GitHub via API pública.")
    query = GetUserReposQuery(service)
    return query.Handle()

@router.post("/store/profile")
def StoreProfile():
    logger.info("Armazenando perfil GitHub no MongoDB.")
    command = StoreUserProfileCommand()
    command.Handle()
    return {"message": "Perfil armazenado no MongoDB"}

@router.post("/store/repos")
def StoreRepos():
    logger.info("Armazenando repositórios GitHub no MongoDB.")
    command = StoreUserReposCommand()
    command.Handle()
    return {"message": "Repositórios armazenados no MongoDB"}

@router.get("/stored/profile")
def GetStoredProfile():
    logger.info("Buscando perfil armazenado no MongoDB.")
    query = GetStoredUserProfileQuery()
    return query.Handle()

@router.get("/stored/repos")
def GetStoredRepos():
    logger.info("Buscando repositórios armazenados no MongoDB.")
    query = GetStoredUserReposQuery()
    return query.Handle()
