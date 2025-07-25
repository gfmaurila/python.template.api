class UserForgotPasswordDomainEvent:
    def __init__(self, Email: str, Code: str):
        self.Email = Email
        self.Code = Code