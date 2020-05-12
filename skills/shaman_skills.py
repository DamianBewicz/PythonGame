from effects import EarthQuakeEffect
from enums import AttackType, MagicNature
from skills.abstract_skills import Heal, MagicDmgDebuff


class HealingRain(Heal):

    def __init__(self, mana_cost: int = 30, hp: int = 20) -> None:
        super().__init__(mana_cost, hp)


class EarthQuake(MagicDmgDebuff):
    TYPE: AttackType = AttackType.MAGIC
    SOURCE: MagicNature = MagicNature.EARTH

    def __init__(self, mana_cost: int = 20, min_dmg: int = 10, max_dmg: int = 20) -> None:
        super().__init__(mana_cost, min_dmg, max_dmg)

    @property
    def effect(self):
        return EarthQuakeEffect()
