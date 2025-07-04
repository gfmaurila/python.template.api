
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API Python Template com DDD, CQRS e Vertical Slices"}

