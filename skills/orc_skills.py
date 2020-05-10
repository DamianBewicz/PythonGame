from effects import FuryEffect
from skills.abstract_skills import Buff


class Fury(Buff):
    def __init__(self, mana_cost=10):
        super().__init__(mana_cost)

    @property
    def effect(self):
        return FuryEffect()
