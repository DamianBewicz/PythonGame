from effects.effects import FuryEffect
from enums import AttackType
from skills.abstract_skills import Buff


class Fury(Buff):
    def __init__(self, mana_cost=10):
        super().__init__(mana_cost)
        self.type = AttackType.BUFF

    @property
    def buff(self):
        return FuryEffect()

    def perform(self, character) -> None:
        if self.buff.is_activated():
            character.effects.append(self.buff)
