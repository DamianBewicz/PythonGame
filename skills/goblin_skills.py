from effects.effects import BleedEffect
from enums import AttackType
from skills.abstract_skills import DmgDebuff


class SpearAttack(DmgDebuff):
    def __init__(self, mana_cost=0, min_dmg=20, max_dmg=30):
        super().__init__(mana_cost, min_dmg, max_dmg)
        self.type = AttackType.PHYSICAL

    @property
    def debuff(self):
        return BleedEffect(duration=5, dmg=10, chance=50)
