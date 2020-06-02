from dmg_object.damage_object import DamageObject
from effects import BleedEffect, BattleShoutEffect
from enums import AttackType
from random import randint
from skills.abstract_skills import Skill, PhysicalDmgDebuff, Buff


class Berserker(Skill):
    TYPE = AttackType.PHYSICAL

    def __init__(self, mana_cost: int=15, min_dmg: int=20, max_dmg: int=30):
        super().__init__(mana_cost)
        self.min_dmg: int = min_dmg
        self.max_dmg: int = max_dmg

    def __str__(self) -> str:
        return "Berserker"

    @property
    def dmg(self) -> int:
        return randint(self.min_dmg, self.max_dmg)

    def perform(self, character) -> None:
        character.take_dmg(DamageObject(dmg=self.dmg, attack_type=self.TYPE))


class BloodySlice(PhysicalDmgDebuff):
    TYPE: AttackType = AttackType.PHYSICAL

    def __init__(self, mana_cost: int = 10, min_dmg: int = 10, max_dmg: int = 15):
        super().__init__(mana_cost, min_dmg, max_dmg)

    def __str__(self) -> str:
        return "Krawe Cięcie"

    @property
    def effect(self):
        return BleedEffect()


class BattleShout(Buff):

    def __init__(self, mana_cost: int = 10) -> None:
        super().__init__(mana_cost)

    def __str__(self) -> str:
        return "Okrzyk Bojowy"

    @property
    def effect(self):
        return BattleShoutEffect()

    def perform(self, character) -> None:
        if self.effect.is_activated():
            character.effects.append(self.effect)
