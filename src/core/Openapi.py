from fastapi.openapi.utils import get_openapi

def CustomOpenapi(app):
    if app.openapi_schema:
        return app.openapi_schema


    openapi_schema = get_openapi(
        title="API Exemple",
        version="v1",
        description="Documentação da API com autenticação JWT.",
        routes=app.routes,
    )

    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }

    for path in openapi_schema["paths"]:
        for method in openapi_schema["paths"][path]:
            openapi_schema["paths"][path][method]["security"] = [{"BearerAuth": []}]

    app.openapi_schema = openapi_schema
    return app.openapi_schema
