from enum import Enum
from typing import Optional
from random import randint


class Skill:
    def __init__(self, mana_cost: int = None) -> None:
        self.mana_cost = mana_cost
        self.type = NotImplemented


class StatusEffect(Skill):
    pass


class Buff(StatusEffect):
    def __init__(self, mana_cost) -> None:
        super().__init__(mana_cost)
        self.type = Type.BUFF

    @property
    def buff(self):
        return NotImplemented

    def perform(self, character) -> None:
        if self.buff.is_activated():
            character.effects.append(self.buff)


class Debuff(StatusEffect):
    def __init__(self, mana_cost) -> None:
        super().__init__(mana_cost)
        self.type = Type.DEBUFF

    @property
    def debuff(self):
        return NotImplemented

    def perform(self, character) -> None:
        if self.debuff.is_activated():
            character.effects.append(self.debuff)


class Heal(Skill):
    def __init__(self, mana_cost) -> None:
        super().__init__(mana_cost)
        self.type = Type.HEAL
        self.hp = NotImplemented

    def perform(self, character) -> None:
        character.heal(self.hp)


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


class DmgDebuff(Debuff):
    def __init__(self, mana_cost, min_dmg, max_dmg) -> None:
        super().__init__(mana_cost)
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        self.type = NotImplemented

    @property
    def dmg(self) -> int:
        return randint(self.min_dmg, self.max_dmg)

    def perform(self, character) -> None:
        super().perform(character)
        character.take_dmg(self.dmg)


class Type(Enum):
    HEAL = "HEAL"
    BUFF = "BUFF"
    PHYSICAL = "PHYSICAL"
    MAGIC = "MAGIC"
    DEBUFF = "DEBUFF"
