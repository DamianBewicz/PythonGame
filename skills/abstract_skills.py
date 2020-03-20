from enum import Enum
from typing import Optional
from random import randint


class Skill:
    def __init__(self, mana_cost=None) -> None:
        self.mana_cost = mana_cost
        self.type = NotImplemented


class DmgDebuff(Skill):
    def __init__(self, mana_cost, min_dmg, max_dmg):
        super().__init__(mana_cost)
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg

    @property
    def dmg(self):
        return randint(self.min_dmg, self.max_dmg)

    @property
    def debuff(self):
        return NotImplemented

    def perform(self, character) -> None:
        if self.debuff.is_activated():
            character.effects.append(self.debuff)
        character.take_dmg(self)


class Buff(Skill):
    def __init__(self, mana_cost) -> None:
        super().__init__(mana_cost)
        self.type = Type.BUFF

    @property
    def buff(self):
        return NotImplemented

    def perform(self, character) -> None:
        return NotImplemented


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
