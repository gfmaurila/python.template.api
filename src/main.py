from fastapi import FastAPI, Request
from contextlib import asynccontextmanager

from fastapi.responses import JSONResponse

from api import MessagingTestController, UserController
from core.Openapi import CustomOpenapi
from fastapi.exceptions import RequestValidationError
from core.response.ExceptionHandler import validation_exception_handler

from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from core.Database import create_database_if_not_exists, create_all_tables_if_not_exists
from infrastructure.database.seeds.SeedUsers import seed_users

from api import RedisPostController
from api import LogController
from api import MessageController
from api.GithubController import router as GithubRouter
from api.AuthController import router as AuthRouter


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
    
app.include_router(AuthRouter)
app.include_router(UserController.router)
app.include_router(MessagingTestController.router)
app.include_router(RedisPostController.router)
app.include_router(LogController.router)
app.include_router(MessageController.router)
app.include_router(GithubRouter)


app.add_exception_handler(RequestValidationError, validation_exception_handler)

ConfigureLogging()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    print("Validation error detail:", exc.errors())  # <-- LOG DO ERRO EXATO
    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "success": False,
            "success_message": None,
            "status_code": 422,
            "errors": [{"message": err["msg"]} for err in exc.errors()],
            "data": None
        },
    )

@app.get("/")
def read_root():
    from loguru import logger
    logger.info("Endpoint raiz acessado.")
    return {"message": "API Python Template com logging em MongoDB"}

# Debug
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8081, reload=False)
