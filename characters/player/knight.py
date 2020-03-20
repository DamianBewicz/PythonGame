from .player import Player
from skills.abstract_skills import SkillSet
from skills.attack_skill import Attack
from skills.knight_skills import Berserker, BloodySlice, BattleShout


class Knight(Player):
    NAME = "Rycerz"

    def __init__(self, name=None):
        super().__init__(name)
        self.name = name
        self.max_hp = 60
        self.max_mana = 25
        self.hp = 60
        self.mana = 25
        self.attack = Attack(10, 10, effects=self.effects)
        self.rest_hp = 15
        self.rest_mana = 5
        self.skills = SkillSet({
            "1": Berserker(),
            "2": BloodySlice(),
            "3": BattleShout(),
        })

    def remove_effect(self, effect):
        if effect.TYPE == "BUFF STATS":
            self.attack.sub(effect)
        super().remove_effect(effect)
