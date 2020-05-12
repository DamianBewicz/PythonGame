from effects import BleedEffect
from enums import AttackType
from skills.abstract_skills import DmgDebuff


class SpearAttack(DmgDebuff):
    TYPE: AttackType = AttackType.PHYSICAL

    def __init__(self, mana_cost: int = 0, min_dmg: int = 20, max_dmg: int = 30):
        super().__init__(mana_cost, min_dmg, max_dmg)

    @property
    def effect(self):
        return BleedEffect(duration=5, dmg=10, chance=50)
