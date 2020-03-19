from effects.effectv import FuryEffect
from skills.abstract_skills import Type, Buff


class Fury(Buff):
    def __init__(self, mana_cost=10):
        super().__init__(mana_cost)
        self.type = Type.BUFF

    @property
    def buff(self):
        return FuryEffect()

    def perform(self, character) -> None:
        if self.buff.is_activated():
            character.add_effect(self.buff)






