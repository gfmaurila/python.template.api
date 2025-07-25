from datetime import datetime

class UserLoggedInDomainEvent:
    def __init__(self, UserId: str, Email: str, Token: str):
        self.UserId = UserId
        self.Email = Email
        self.Token = Token
        self.OccurredOn = datetime.utcnow()
