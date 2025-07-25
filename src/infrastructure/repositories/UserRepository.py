# src/infrastructure/repositories/UserRepository.py

from typing import List, Optional
from sqlalchemy.orm import Session
from domain.entities.User.UserEntity import UserEntity
from domain.interfaces.IUserRepository import IUserRepository
from infrastructure.database.models.UserModel import UserModel
from domain.valueobjects.Email import Email
from domain.valueobjects.PhoneNumber import PhoneNumber
from domain.enums.ENotificationType import ENotificationType
from domain.enums.EGender import EGender
from core.Database import SessionLocal
from core.util.Password import Password

class UserRepository(IUserRepository):
    def __init__(self):
        self._db: Session = SessionLocal()

    async def Add(self, user: UserEntity) -> None:
        model = UserModel(
            Name=user.Name,
            Email=user.Email.address,
            Senha=user.Senha,
            Phone=user.Phone.phone,
            Notification=user.Notification.value,
            Gender=user.Gender.value
        )
        self._db.add(model)
        self._db.commit()
        self._db.refresh(model)
        user.Id = model.Id

    async def GetAll(self) -> List[UserEntity]:
        results = self._db.query(UserModel).all()
        return [
            UserEntity(
                Id=row.Id,
                Name=row.Name,
                Email=Email(row.Email),
                Senha=row.Senha,
                Phone=PhoneNumber(row.Phone),
                Notification=ENotificationType(row.Notification),
                Gender=EGender(row.Gender)
            )
            for row in results
        ]

    async def GetById(self, userId: int) -> Optional[UserEntity]:
        row = self._db.query(UserModel).filter(UserModel.Id == userId).first()
        if not row:
            return None
        return UserEntity(
            Id=row.Id,
            Name=row.Name,
            Email=Email(row.Email),
            Senha=row.Senha,
            Phone=PhoneNumber(row.Phone),
            Notification=ENotificationType(row.Notification),
            Gender=EGender(row.Gender)
        )

    async def Update(self, userId: int, user: UserEntity) -> None:
        row = self._db.query(UserModel).filter(UserModel.Id == userId).first()
        if row:
            row.Name = user.Name
            row.Email = user.Email.address
            row.Senha = user.Senha
            row.Phone = user.Phone.phone
            row.Notification = user.Notification.value
            row.Gender = user.Gender.value
            self._db.commit()

    async def Delete(self, userId: int) -> None:
        row = self._db.query(UserModel).filter(UserModel.Id == userId).first()
        if row:
            self._db.delete(row)
            self._db.commit()

    async def GetAuthByEmailPassword(self, email: str, password: str) -> Optional[UserEntity]:
        hashed_password = Password.ComputeSha256Hash(password)
        row = self._db.query(UserModel).filter(
            UserModel.Email == email,
            UserModel.Senha == hashed_password
        ).first()

        if not row:
            return None

        return UserEntity(
            Id=row.Id,
            Name=row.Name,
            Email=Email(row.Email),
            Senha=row.Senha,
            Phone=PhoneNumber(row.Phone),
            Notification=ENotificationType(row.Notification),
            Gender=EGender(row.Gender)
        )
    
    async def GetByEmail(self, email: str) -> Optional[UserEntity]:
        row = self._db.query(UserModel).filter(UserModel.Email == email).first()
        if not row:
            return None

        return UserEntity(
            Id=row.Id,
            Name=row.Name,
            Email=Email(row.Email),
            Senha=row.Senha,
            Phone=PhoneNumber(row.Phone),
            Notification=ENotificationType(row.Notification),
            Gender=EGender(row.Gender)
        )
    
    async def Exists(self, userId: int) -> bool:
        exists = self._db.query(UserModel).filter(UserModel.Id == userId).first()
        return exists is not None
    
    