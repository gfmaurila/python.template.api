from uuid import UUID
from typing import List
from Common.Response.ApiResult import ApiResult
from Common.Domain.Enumerado.EGender import EGender
from Common.Domain.Enumerado.ENotificationType import ENotificationType
from Feature.Exemple.Commands.Update.UpdateExempleResponse import UpdateExempleResponse


class UpdateExempleCommand:
    """
    Represents the command to update an existing Exemple entity.
    """

    def __init__(self,
                 Id: UUID,
                 FirstName: str,
                 LastName: str,
                 Status: bool,
                 Gender: EGender,
                 Notification: ENotificationType,
                 Email: str,
                 Phone: str,
                 Role: List[str]):

        self.Id = Id
        self.FirstName = FirstName
        self.LastName = LastName
        self.Status = Status
        self.Gender = Gender
        self.Notification = Notification
        self.Email = Email
        self.Phone = Phone
        self.Role = Role
