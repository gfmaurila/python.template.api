class UserPasswordResetDomainEvent:
    def __init__(self, UserId: int):
        self.UserId = UserId