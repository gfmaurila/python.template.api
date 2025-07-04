
# http://127.0.0.1:8081/docs
# uvicorn Main:app --reload --port 8081



from fastapi import FastAPI, Depends
from Extensions.Swagger import custom_openapi
from Extensions.Settings import settings
from Extensions.Auth import verify_jwt

app = FastAPI()

# Override padrão OpenAPI
app.openapi = lambda: custom_openapi(app)

@app.get("/ping", dependencies=[Depends(verify_jwt)])
def ping():
    return {"message": "pong"}



