# src/infrastructure/database/models/UserModel.py

from sqlalchemy import Column, Integer, String
from core.Database import Base
from domain.enums.ENotificationType import ENotificationType
from domain.enums.EGender import EGender

class UserModel(Base):
    __tablename__ = "TB_USER"

    Id = Column(Integer, primary_key=True, index=True)
    Name = Column(String(100), nullable=False)
    Email = Column(String(100), nullable=False)
    Senha = Column(String(100), nullable=False)
    Phone = Column(String(20), nullable=True)
    Notification = Column(Integer, nullable=False)  # armazenado como int
    Gender = Column(Integer, nullable=False)        # armazenado como int

