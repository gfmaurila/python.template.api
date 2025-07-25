# src/api/dependencies/gender_parser.py

from domain.enums.EGender import EGender
from fastapi import Query, HTTPException
from typing import Optional

def parse_gender(value: Optional[str]) -> Optional[EGender]:
    if value is None:
        return None

    # Aceita string (case-insensitive)
    value_lower = value.lower()
    if value_lower in ["male", "1"]:
        return EGender.Male
    elif value_lower in ["female", "2"]:
        return EGender.Female
    elif value_lower in ["none", "0"]:
        return EGender.None_

    # Aceita diretamente número
    try:
        return EGender(int(value))
    except:
        raise HTTPException(status_code=422, detail=f"Invalid gender value: {value}")
