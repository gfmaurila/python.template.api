from enum import Enum


class EGender(int, Enum):
    """
    Represents the gender options.
    """
    None_ = 0  # "None" é palavra reservada, então usamos "None_"
    Male = 1
    Female = 2

    @property
    def description(self) -> str:
        return {
            EGender.None_: "Não informar",
            EGender.Male: "Male",
            EGender.Female: "Female"
        }[self]
