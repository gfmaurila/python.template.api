# src/domain/enums/EGender.py

from enum import IntEnum

class EGender(IntEnum):
    """
    Represents the gender options.
    """

    None_ = 0
    Male = 1
    Female = 2

    def description(self) -> str:
        descriptions = {
            EGender.None_: "Não informar",
            EGender.Male: "Male",
            EGender.Female: "Female",
        }
        return descriptions.get(self, "Unknown")

    def __str__(self):
        return self.description()
