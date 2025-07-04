
# main.py



from fastapi import FastAPI

from api import UserController

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API Python Template com DDD, CQRS e Vertical Slices"}


app.include_router(UserController.router)

