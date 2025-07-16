from fastapi import FastAPI
from contextlib import asynccontextmanager

from api import MessagingTestController, UserController
from core.Openapi import CustomOpenapi
from fastapi.exceptions import RequestValidationError
from core.response.ExceptionHandler import validation_exception_handler

from core.Database import create_database_if_not_exists, create_all_tables_if_not_exists
from infrastructure.database.seeds.SeedUsers import seed_users

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_database_if_not_exists()
    create_all_tables_if_not_exists()
    seed_users()
    yield  # Aqui o app inicia
    # Aqui você pode fazer cleanup, se necessário

app = FastAPI(lifespan=lifespan)
app.openapi = lambda: CustomOpenapi(app)

@app.get("/")
def read_root():
    return {"message": "API Python Template com DDD, CQRS e Vertical Slices"}

app.include_router(UserController.router)
app.include_router(MessagingTestController.router)

app.add_exception_handler(RequestValidationError, validation_exception_handler)
