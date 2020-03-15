from enum import Enum
from typing import Optional


class Skill:
    def __init__(self, mana_cost=None) -> None:
        self.mana_cost = mana_cost
        self.type = NotImplemented


class SkillSet:
    def __init__(self, skills=None) -> None:
        self.skills = skills

    def introduce(self) -> None:
        for number, skill in self.skills.items():
            print(number, skill)

    def choose(self) -> Optional[Skill]:
        while True:
            self.introduce()
            choice = input("\nWybierz umiejętność, jeśli chcesz wyjść naciśnij enter\n")
            try:
                if choice == "":
                    return None
                return self.skills[choice]
            except KeyError:
                print("\nPodana wartość jest nieprawidłowa, proszę podać cyfrę!\n")


class Type(Enum):
    HEAL = "HEAL"
    BUFF = "BUFF"
    PHYSICAL = "PHYSICAL"
    MAGIC = "MAGIC"
