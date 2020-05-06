from math import floor
from random import randint
from effects.effects import CurseEffect
from enums import AttackType


class Attack:
    def __init__(self, min_dmg=None, max_dmg=None, effects=None) -> None:
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        self.type = AttackType.NORMAL
        self.effects = effects

    @property
    def dmg(self) -> int:
        percent_damage_reduction = 1
        if self.effects.contains(CurseEffect):
            percent_damage_reduction = self.effects.get_effect(CurseEffect).get_damage_reduction()
        bonus_dmg = {
            "min_dmg": 0,
            "max_dmg": 0,
        }
        if self.effects.contains_stats_effect():
            bonus_dmg = self.count_bonus_dmg()
        return floor(percent_damage_reduction * randint(self.min_dmg + bonus_dmg["min_dmg"], self.max_dmg + bonus_dmg["max_dmg"]))

    def perform(self, character) -> None:
        character.take_dmg(self.dmg)

    def count_bonus_dmg(self) -> dict:
        bonus_min_dmg = 0
        bonus_max_dmg = 0
        for effect in self.effects.stats_effects():
            bonus_min_dmg += effect.min_dmg
            bonus_max_dmg += effect.max_dmg
        return {"min_dmg": bonus_min_dmg, "max_dmg": bonus_max_dmg}
