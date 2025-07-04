from enum import Enum

class EGender(Enum):
    """
    Represents the gender options.
    """
    
    None_ = (0, "Não informar")
    Male = (1, "Male")
    Female = (2, "Female")

    def __init__(self, value: int, description: str):
        self._value_ = value
        self.description = description

    def __str__(self):
        return self.description
