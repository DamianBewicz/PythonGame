from random import randint

from skills.abstract_skills import Type


class Attack:
    def __init__(self, min_dmg=None, max_dmg=None, type=Type.PHYSICAL, effects=None):
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        self.type = type
        self.effects = effects

    @property
    def dmg(self):
        return randint(self.min_dmg, self.max_dmg)

    def perform(self, character):
        character.take_dmg(self)

    def bonus_dmg(self):
        min_bonus_dmg = 0
        max_bonus_dmg = 0
        iter_ = self.effects.stats_effects()
        print(list(iter_))
