# src/application/User/dtos/UserQueryModel.py

from pydantic import BaseModel
from domain.entities.User.UserEntity import UserEntity


class UserQueryModel(BaseModel):
    Id: int
    Name: str
    Email: str
    Phone: str
    Notification: int
    Gender: int

    @classmethod
    def from_entity(cls, entity: UserEntity) -> "UserQueryModel":
        return cls(
            Id=entity.Id,
            Name=entity.Name,
            Email=str(entity.Email),
            Phone=str(entity.Phone),
            Notification=entity.Notification.value,
            Gender=entity.Gender.value
        )
