from sqlalchemy.orm import Session
from core.Database import engine
from infrastructure.database.models.UserModel import UserModel
from domain.enums.ENotificationType import ENotificationType
from domain.enums.EGender import EGender

def seed_users():
    users = [
        UserModel(Name="João Silva", Email="joao@example.com", Senha="123456", Phone="11999990001", Notification=ENotificationType.Email.value, Gender=EGender.Male.value),
        UserModel(Name="Maria Oliveira", Email="maria@example.com", Senha="abcdef", Phone="11999990002", Notification=ENotificationType.SMS.value, Gender=EGender.Female.value),
        UserModel(Name="Carlos Souza", Email="carlos@example.com", Senha="senha123", Phone="11999990003", Notification=ENotificationType.WhatsApp.value, Gender=EGender.Male.value),
        UserModel(Name="Ana Costa", Email="ana@example.com", Senha="ana321", Phone="11999990004", Notification=ENotificationType.Email.value, Gender=EGender.Female.value),
        UserModel(Name="Pedro Rocha", Email="pedro@example.com", Senha="pedropass", Phone="11999990005", Notification=ENotificationType.SMS.value, Gender=EGender.Male.value),
    ]

    with Session(engine) as session:
        existing = session.query(UserModel).first()
        if not existing:
            session.bulk_save_objects(users)
            session.commit()
            print("Usuários de teste inseridos com sucesso.")
        else:
            print("Usuários já existem. Seed ignorado.")
