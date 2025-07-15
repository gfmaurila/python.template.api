from pydantic import BaseModel, EmailStr, Field, field_validator
from domain.enums.ENotificationType import ENotificationType
from domain.enums.EGender import EGender
import re


class UserDto(BaseModel):
    Name: str = Field(..., max_length=100, min_length=1)
    Email: EmailStr = Field(..., max_length=254)
    Senha: str = Field(..., min_length=6, max_length=100)
    Phone: str = Field(..., min_length=8, max_length=20)
    Notification: ENotificationType
    Gender: EGender

    @field_validator('Senha')
    @classmethod
    def validar_senha(cls, value: str) -> str:
        # Requisitos básicos
        if not re.search(r"[A-Z]", value):
            raise ValueError("A senha deve conter pelo menos uma letra maiúscula.")
        if not re.search(r"[a-z]", value):
            raise ValueError("A senha deve conter pelo menos uma letra minúscula.")
        if not re.search(r"\d", value):
            raise ValueError("A senha deve conter pelo menos um número.")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>_\[\]\\/~\-+=]", value):
            raise ValueError("A senha deve conter pelo menos um caractere especial.")

        # Verificar sequências numéricas (ex: 123456)
        numeros = re.sub(r"[^\d]", "", value)
        if cls._tem_sequencia(numeros):
            raise ValueError("A senha não pode conter números em sequência crescente.")

        # Verificar sequências de letras (ex: abcdef)
        letras = re.sub(r"[^a-zA-Z]", "", value).lower()
        if cls._tem_sequencia(letras):
            raise ValueError("A senha não pode conter letras em sequência crescente.")

        return value

    @staticmethod
    def _tem_sequencia(texto: str, tamanho_min: int = 3) -> bool:
        for i in range(len(texto) - tamanho_min + 1):
            trecho = texto[i:i + tamanho_min]
            if all(ord(trecho[j]) == ord(trecho[j - 1]) + 1 for j in range(1, len(trecho))):
                return True
        return False

    @field_validator('Phone')
    @classmethod
    def phone_must_be_numeric(cls, value):
        if not value.isdigit():
            raise ValueError("O telefone deve conter apenas números.")
        return value

    @field_validator('Gender')
    @classmethod
    def gender_must_be_valid(cls, value: EGender):
        if value.value == 0:
            raise ValueError("Selecione um gênero válido. 'Não informar' não é permitido.")
        return value
