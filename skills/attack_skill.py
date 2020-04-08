from random import randint

from skills.abstract_skills import Type


class Attack:
    def __init__(self, min_dmg=None, max_dmg=None, effects=None, type=Type.PHYSICAL):
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        self.type = type
        self.effects = effects

    @property
    def dmg(self):
        if self.effects.contains_stats_effect():
            bonus_dmg = self.count_bonus_dmg()
            print(bonus_dmg)
            return randint(self.min_dmg + bonus_dmg["min_dmg"], self.max_dmg + bonus_dmg["max_dmg"])
        return randint(self.min_dmg, self.max_dmg)

    def perform(self, character):
        character.take_dmg(self)

    def count_bonus_dmg(self):
        bonus_min_dmg = 0
        bonus_max_dmg = 0
        for effect in self.effects.stats_effects():
            bonus_min_dmg += effect.min_dmg
            bonus_max_dmg += effect.max_dmg
        return {"min_dmg": bonus_min_dmg, "max_dmg": bonus_max_dmg}
