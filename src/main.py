from fastapi import FastAPI
from api import MessagingTestController, UserController
from core.Openapi import CustomOpenapi
from fastapi.exceptions import RequestValidationError
from core.response.ExceptionHandler import validation_exception_handler

app = FastAPI()
app.openapi = lambda: CustomOpenapi(app)

@app.get("/")
def read_root():
    return {"message": "API Python Template com DDD, CQRS e Vertical Slices"}

app.include_router(UserController.router)
app.include_router(MessagingTestController.router)

# Registrar handler global para erros de validação
app.add_exception_handler(RequestValidationError, validation_exception_handler)

import sys
print(sys.path)