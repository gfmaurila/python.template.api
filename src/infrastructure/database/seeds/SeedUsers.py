from sqlalchemy.orm import Session
from core.Database import engine
from core.util.Password import Password
from infrastructure.database.models.UserModel import UserModel
from domain.enums.ENotificationType import ENotificationType
from domain.enums.EGender import EGender

from application.User.dtos.UserQueryModel import UserQueryModel
from infrastructure.service.RedisCacheService import RedisCacheService
from core.domain.model.CacheOptions import CacheOptions
from core.Config import GetSettings

import asyncio
import json

def seed_users():
    users = [
        UserModel(Name="João Silva", Email="joao@example.com", Senha=Password.ComputeSha256Hash("123456"), Phone="11999990001", Notification=ENotificationType.Email.value, Gender=EGender.Male.value),
        UserModel(Name="Maria Oliveira", Email="maria@example.com", Senha=Password.ComputeSha256Hash("abcdef"), Phone="11999990002", Notification=ENotificationType.SMS.value, Gender=EGender.Female.value),
        UserModel(Name="Carlos Souza", Email="carlos@example.com", Senha=Password.ComputeSha256Hash("senha123"), Phone="11999990003", Notification=ENotificationType.WhatsApp.value, Gender=EGender.Male.value),
        UserModel(Name="Ana Costa", Email="ana@example.com", Senha=Password.ComputeSha256Hash("ana321"), Phone="11999990004", Notification=ENotificationType.Email.value, Gender=EGender.Female.value),
        UserModel(Name="Pedro Rocha", Email="pedro@example.com", Senha=Password.ComputeSha256Hash("pedropass"), Phone="11999990005", Notification=ENotificationType.SMS.value, Gender=EGender.Male.value),
        UserModel(Name="Guilherme F Maurila", Email="gfmaurila@gmail.com", Senha=Password.ComputeSha256Hash("@G18u03i1986"), Phone="11999999999", Notification=ENotificationType.Email.value, Gender=EGender.Male.value),
    ]

    with Session(engine) as session:
        existing = session.query(UserModel).first()
        if not existing:
            session.bulk_save_objects(users)
            session.commit()
            print("Usuários de teste inseridos com sucesso.")

            # Salvar também no Redis
            asyncio.run(_cache_seeded_users(users))
        else:
            print("Usuários já existem. Seed ignorado.")


async def _cache_seeded_users(users: list[UserModel]):
    settings = GetSettings()

    cacheOptions = CacheOptions(
        DbIndex=settings.REDIS_DB,
        AbsoluteExpirationInHours=0,
        SlidingExpirationInSeconds=0
    )
    redisUrl = f"redis://:{settings.REDIS_PASSWORD}@{settings.REDIS_HOST}:{settings.REDIS_PORT}/{settings.REDIS_DB_USER}"

    cacheService = RedisCacheService(
        cacheOptions=cacheOptions,
        redisUrl=redisUrl
    )

    for user in users:
        user_dict = UserQueryModel(
            Id=user.Id,
            Name=user.Name,
            Email=user.Email,
            Phone=user.Phone,
            Notification=user.Notification,
            Gender=user.Gender
        ).model_dump()

        await cacheService.SetAsync(
            key=f"UserSeeded:{user.Id}",
            value=user_dict,
            expiry=None  # sem expiração
        )

    print(f"{len(users)} usuários também foram salvos no Redis.")
