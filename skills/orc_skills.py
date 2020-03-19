from effects.effectv import RevengeEffect
from skills.abstract_skills import Skill, Type


class Revenge(Skill):
    def __init__(self, mana_cost=10):
        super().__init__(mana_cost)
        self.type = Type.BUFF

    @property
    def buff(self):
        return RevengeEffect()


