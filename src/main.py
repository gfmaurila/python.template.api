from fastapi import FastAPI
from contextlib import asynccontextmanager

from api import MessagingTestController, UserController
from core.Openapi import CustomOpenapi
from fastapi.exceptions import RequestValidationError
from core.response.ExceptionHandler import validation_exception_handler

from core.Database import create_database_if_not_exists, create_all_tables_if_not_exists
from infrastructure.database.seeds.SeedUsers import seed_users

from api import RedisPostController
from api import LogController

from fastapi import FastAPI
from infrastructure.logging.MongoLogger import ConfigureLogging

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
app.include_router(RedisPostController.router)
app.include_router(LogController.router)

app.add_exception_handler(RequestValidationError, validation_exception_handler)

ConfigureLogging()

@app.get("/")
def read_root():
    from loguru import logger
    logger.info("Endpoint raiz acessado.")
    return {"message": "API Python Template com logging em MongoDB"}

# Debug
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8081, reload=False)
