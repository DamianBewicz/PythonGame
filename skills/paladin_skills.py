from effects.abstract_effects import Effect
from effects.effects import HolyShieldEffect
from skills.abstract_skills import Skill, AttackType, Heal
from random import randint


class HolyLight(Heal):
    def __init__(self, mana_cost=20) -> None:
        super().__init__(mana_cost)
        self.hp = 30

    def __str__(self) -> str:
        return "Święty Blask"


class HammerTime(Skill):
    def __init__(self, mana_cost=15):
        super().__init__(mana_cost)
        self.type = AttackType.MAGIC
        self.min_dmg = 10
        self.max_dmg = 25

    def __str__(self) -> str:
        return "Czas Młota!"

    @property
    def dmg(self) -> int:
        return randint(self.min_dmg, self.max_dmg)

    def perform(self, character) -> None:
        character.take_dmg(self.dmg)


class HolyShield(Skill):
    def __init__(self, mana_cost=20) -> None:
        super().__init__(mana_cost)
        self.type = AttackType.BUFF

    def __str__(self) -> str:
        return "Święta Tarcza"

    @property
    def buff(self) -> Effect:
        return HolyShieldEffect()

    def perform(self, character) -> None:
        if self.buff.is_activated():
            character.effects.append(self.buff)
