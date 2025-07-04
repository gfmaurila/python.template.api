
# src/domain/entities/user.py

class User:
    def __init__(self, Id: int, Name: str, Email: str):
        self.Id = Id
        self.Name = Name
        self.Email = Email

    