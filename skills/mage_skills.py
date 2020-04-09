from effects.abstract_effects import Effect
from effects.effects import BurnEffect, FireShieldEffect, Blind
from skills.abstract_skills import Skill, Type
from random import randint


class Fireball(Skill):

    def __init__(self, mana_cost=20) -> None:
        super().__init__(mana_cost)
        self.type = Type.MAGIC
        self.min_dmg = 25
        self.max_dmg = 40

    def __str__(self) -> str:
        return "Kula Ognia"

    @property
    def dmg(self) -> int:
        return randint(self.min_dmg, self.max_dmg)

    @property
    def debuff(self) -> Effect:
        return BurnEffect()

    def perform(self, character) -> None:
        if self.debuff.is_activated():
            character.effects.append(self.debuff)
        character.take_dmg(self.dmg)


class FireShield(Skill):
    def __init__(self, mana_cost=20) -> None:
        super().__init__(mana_cost)
        self.type = Type.BUFF

    def __str__(self) -> str:
        return "Ogniowa Tarcza"

    @property
    def buff(self) -> Effect:
        return FireShieldEffect()

    def perform(self, character) -> None:
        if self.buff.is_activated():
            character.effects.append(self.buff)


class Lightining(Skill):
    def __init__(self, mana_cost=30) -> None:
        super().__init__(mana_cost)
        self.type = Type.MAGIC
        self.min_dmg = 15
        self.max_dmg = 25

    @property
    def dmg(self) -> int:
        return randint(self.min_dmg, self.max_dmg)

    @property
    def debuff(self) -> Effect:
        return Blind()

    def __str__(self) -> str:
        return "Błyskawica"

    def perform(self, character) -> None:
        if self.debuff.is_activated():
            character.effects.append(self.debuff)
        character.take_dmg(self.dmg)
