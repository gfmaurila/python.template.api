from typing import List
from Common.Domain.Enumerado.EGender import EGender
from Common.Domain.Enumerado.ENotificationType import ENotificationType


class CreateExempleCommand:
    """
    Command to create a new Exemple entity.
    """

    def __init__(self,
                 FirstName: str,
                 LastName: str,
                 Status: bool,
                 Gender: EGender,
                 Notification: ENotificationType,
                 Email: str,
                 Phone: str,
                 Role: List[str]):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Status = Status
        self.Gender = Gender
        self.Notification = Notification
        self.Email = Email
        self.Phone = Phone
        self.Role = Role
