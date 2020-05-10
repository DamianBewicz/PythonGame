from effects import EarthQuakeEffect
from enums import AttackType, MagicNature
from skills.abstract_skills import Heal, MagicDmgDebuff


class HealingRain(Heal):

    def __init__(self, mana_cost=30, hp=20) -> None:
        super().__init__(mana_cost, hp)


class EarthQuake(MagicDmgDebuff):
    TYPE = AttackType.MAGIC
    SOURCE = MagicNature.EARTH

    def __init__(self, mana_cost=20, min_dmg=10, max_dmg=20):
        super().__init__(mana_cost, min_dmg, max_dmg)

    @property
    def effect(self):
        return EarthQuakeEffect()
