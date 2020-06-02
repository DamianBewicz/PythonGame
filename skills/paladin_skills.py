from dmg_object.damage_object import DamageObject
from effects import HolyShieldEffect
from effects.abstract_effects import Effect
from enums import AttackType, MagicNature
from random import randint
from skills.abstract_skills import Heal, Skill, Buff


class HolyLight(Heal):
    def __init__(self, mana_cost: int = 20, heal: int = 30) -> None:
        super().__init__(mana_cost, heal)

    def __str__(self) -> str:
        return "Święty Blask"


class HammerTime(Skill):
    TYPE: AttackType = AttackType.MAGIC
    SOURCE: MagicNature = MagicNature.LIGHTNING

    def __init__(self, mana_cost: int = 15):
        super().__init__(mana_cost)
        self.min_dmg = 10
        self.max_dmg = 25

    def __str__(self) -> str:
        return "Czas Młota!"

    @property
    def dmg(self) -> int:
        return randint(self.min_dmg, self.max_dmg)

    def perform(self, character) -> None:
        character.take_dmg(DamageObject(dmg=self.dmg, attack_type=self.TYPE, source=self.SOURCE))


class HolyShield(Buff):
    def __init__(self, mana_cost: int = 20) -> None:
        super().__init__(mana_cost)
        self.type: AttackType = AttackType.BUFF

    def __str__(self) -> str:
        return "Święta Tarcza"

    @property
    def effect(self) -> Effect:
        return HolyShieldEffect()

    def perform(self, character) -> None:
        if self.effect.is_activated():
            character.effects.append(self.effect)
