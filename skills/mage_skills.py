from dmg_object.damage_object import DamageObject
from effects import BurnEffect, FireShieldEffect, Blind
from effects.abstract_effects import Effect
from enums import MagicNature
from random import randint
from skills.abstract_skills import MagicDmgDebuff, Buff


class Fireball(MagicDmgDebuff):
    SOURCE: MagicNature = MagicNature.FIRE

    def __init__(self, mana_cost: int = 20, min_dmg: int = 25, max_dmg: int = 40) -> None:
        super().__init__(mana_cost, min_dmg, max_dmg)

    def __str__(self) -> str:
        return "Kula Ognia"

    @property
    def dmg(self) -> int:
        return randint(self.min_dmg, self.max_dmg)

    @property
    def effect(self) -> Effect:
        return BurnEffect()

    def perform(self, character) -> None:
        if self.effect.is_activated():
            character.effects.append(self.effect)
        character.take_dmg(DamageObject(dmg=self.dmg, attack_type=self.ATTACK_TYPE, source=self.SOURCE))


class FireShield(Buff):

    def __init__(self, mana_cost: int = 20) -> None:
        super().__init__(mana_cost)

    def __str__(self) -> str:
        return "Ogniowa Tarcza"

    @property
    def effect(self) -> Effect:
        return FireShieldEffect()


class Lightining(MagicDmgDebuff):

    def __init__(self, mana_cost: int = 30, min_dmg: int = 15, max_dmg: int = 25) -> None:
        super().__init__(mana_cost, min_dmg, max_dmg)

    @property
    def effect(self) -> Effect:
        return Blind()

    def __str__(self) -> str:
        return "Błyskawica"
