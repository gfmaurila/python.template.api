
# src/domain/entities/user.py

# class User:
#     def __init__(self, Id: int, Name: str, Email: str):
#         self.Id = Id
#         self.Name = Name
#         self.Email = Email

# src/domain/entities/user.py

from domain.valueobjects.Email import Email
from domain.valueobjects.PhoneNumber import PhoneNumber
from domain.enums.ENotificationType import ENotificationType
from domain.enums.EGender import EGender


class User:
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
        self.Id = Id
        self.Name = Name
        self.Email = Email
        self.Senha = Senha
        self.Phone = Phone
        self.Notification = Notification
        self.Gender = Gender
    