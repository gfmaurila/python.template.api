
# http://127.0.0.1:8081/docs
# uvicorn Main:app --reload --port 8081



from fastapi import FastAPI, Depends
from Extensions.Swagger import custom_openapi
from Extensions.Settings import settings
from Extensions.Auth import verify_jwt

from pydantic import BaseModel

app = FastAPI()

# Override padrão OpenAPI
app.openapi = lambda: custom_openapi(app)

@app.get("/ping", dependencies=[Depends(verify_jwt)])
def ping():
    return {"message": "pong"}


# Modelo de entrada
class PublicInput(BaseModel):
    Nome: str
    Email: str

# Endpoint POST sem autenticação
@app.post("/public")
def PublicPost(data: PublicInput):
    return {
        "message": "Recebido com sucesso!",
        "nome": data.Nome,
        "email": data.Email
    }


from Extensions.Settings import settings



print(settings.SQL_CONNECTION)
print(settings.JWT_KEY)
print(settings.RABBIT_HOST)
print(settings.KAFKA_TOPIC)
print(settings.API_AUTH_URL)

