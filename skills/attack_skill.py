from random import randint

from skills.abstract_skills import Type


class Attack:
    def __init__(self, min_dmg=None, max_dmg=None, type=Type.PHYSICAL):
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        self.type = type

    @property
    def dmg(self):
        return randint(self.min_dmg, self.max_dmg)

    def perform(self, character):
        character.take_dmg(self)

    def add(self, effect):
        self.min_dmg += effect.min_dmg
        self.max_dmg += effect.max_dmg

    def sub(self, effect):
        self.min_dmg -= effect.min_dmg
        self.max_dmg -= effect.max_dmg
