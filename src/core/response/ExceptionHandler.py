from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from core.response.ApiResult import ApiResult, ErrorDetail

# Traduções (como você já fez)
TRADUCOES_ERROS = {
    "missing": "Campo obrigatório.",
    "value_error.missing": "Campo obrigatório.",
    "string_too_short": "O valor deve conter pelo menos {min_length} caracteres.",
    "string_too_long": "O valor deve conter no máximo {max_length} caracteres.",
    "value_error.any_str.min_length": "O valor deve conter pelo menos {limit_value} caracteres.",
    "value_error.any_str.max_length": "O valor deve conter no máximo {limit_value} caracteres.",
    "type_error.str": "O valor deve ser uma string.",
    "value_error.email": "E-mail inválido.",
    "type_error.email": "E-mail inválido.",
    "value_error.number.not_ge": "O valor deve ser maior ou igual a {ge}.",
    "value_error.number.not_gt": "O valor deve ser maior que {gt}.",
    "value_error.number.not_le": "O valor deve ser menor ou igual a {le}.",
    "value_error.number.not_lt": "O valor deve ser menor que {lt}.",
    "type_error.int": "O valor deve ser um número inteiro.",
    "type_error.float": "O valor deve ser um número decimal.",
    "type_error.bool": "O valor deve ser verdadeiro ou falso.",
    "type_error.list": "O valor deve ser uma lista.",
    "value_error.list.min_items": "A lista deve conter pelo menos {limit_value} itens.",
    "value_error.list.max_items": "A lista deve conter no máximo {limit_value} itens.",
    "type_error.enum": "O valor informado não é uma opção válida.",
    "value_error.date": "A data informada é inválida.",
    "type_error.date": "O valor deve ser uma data (yyyy-mm-dd).",
    "value_error.datetime": "O valor deve ser uma data e hora válida.",
    "type_error.datetime": "O valor deve ser uma data e hora no formato ISO.",
    "value_error.str.regex": "O valor não corresponde ao formato esperado.",
    "value_error.any": "Valor inválido.",
    "type_error.none.not_allowed": "Este campo não pode ser nulo.",
}


def traduzir_mensagem(erro: dict) -> str:
    tipo = erro.get("type")
    msg = erro.get("msg")
    ctx = erro.get("ctx", {})

    if tipo in TRADUCOES_ERROS:
        return TRADUCOES_ERROS[tipo].format(**ctx)
    elif "value_error.email" in tipo:
        return TRADUCOES_ERROS["value_error.email"]
    elif "missing" in tipo or msg == "Field required":
        return TRADUCOES_ERROS["missing"]
    return msg


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = [ErrorDetail(message=traduzir_mensagem(err)) for err in exc.errors()]
    result = ApiResult.create_error(errors, HTTP_422_UNPROCESSABLE_ENTITY)
    return JSONResponse(
        status_code=result.status_code,
        content=result.model_dump()
    )
