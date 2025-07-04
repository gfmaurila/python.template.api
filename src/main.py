
# main.py



from fastapi import FastAPI

from api import UserController
from core.Openapi import CustomOpenapi

app = FastAPI()

app.openapi = lambda: CustomOpenapi(app)

@app.get("/")
def read_root():
    return {"message": "API Python Template com DDD, CQRS e Vertical Slices"}

app.include_router(UserController.router)

