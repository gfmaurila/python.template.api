from application.Auth.dtos.AuthCommand import AuthCommand
from pydantic import ValidationError
from fastapi import HTTPException

class AuthCommandValidator:
    def Validate(self, command: AuthCommand):
        try:
            command_dict = command.dict()
            AuthCommand(**command_dict)
        except ValidationError as e:
            raise HTTPException(status_code=400, detail=e.errors())
