# src/domain/entities/User.py

from core.domain.entities.BaseEntity import BaseEntity
from core.domain.interfaces.IAggregateRoot import IAggregateRoot
from domain.valueobjects.Email import Email
from domain.valueobjects.PhoneNumber import PhoneNumber
from domain.enums.ENotificationType import ENotificationType
from domain.enums.EGender import EGender
from domain.entities.User.events.UserCreatedDomainEvent import UserCreatedDomainEvent

class UserEntity(BaseEntity, IAggregateRoot):
    def __init__(
        self,
        Id: int,
        Name: str,
        Email: Email,
        Senha: str,
        Phone: PhoneNumber,
        Notification: ENotificationType,
        Gender: EGender,
    ):
        super().__init__()
        self.Id = Id
        self.Name = Name
        self.Email = Email
        self.Senha = Senha
        self.Phone = Phone
        self.Notification = Notification
        self.Gender = Gender

        self.AddDomainEvent(UserCreatedDomainEvent(
            Id=self.Id,
            Name=self.Name,
            Email=self.Email.address,  # <- CORRIGIDO
            Phone=self.Phone.phone,    # <- se necessário
            Notification=self.Notification,
            Gender=self.Gender
        ))
