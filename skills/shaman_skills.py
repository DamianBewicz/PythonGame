from random import randint
from effects.effects import EarthQuakeEffect
from enums import AttackType
from skills.abstract_skills import Heal, DmgDebuff


class HealingRain(Heal):

    def __init__(self, mana_cost=30) -> None:
        super().__init__(mana_cost)
        self.hp = 20

    def perform(self, character) -> None:
        character.heal(self)


class EarthQuake(DmgDebuff):

    def __init__(self, mana_cost=20, min_dmg=10, max_dmg=20):
        super().__init__(mana_cost, min_dmg, max_dmg)
        self.type = AttackType.MAGIC

    @property
    def dmg(self):
        return randint(self.min_dmg, self.max_dmg)

    @property
    def debuff(self):
        return EarthQuakeEffect()

    def perform(self, character) -> None:
        if self.debuff.is_activated():
            character.effects.append(self.debuff)
        character.take_dmg(self.dmg)
