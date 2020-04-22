from enums import PlayerClasses
from .player import Player
from skills.abstract_skills import SkillSet
from skills.attack_skill import Attack
from skills.knight_skills import Berserker, BloodySlice, BattleShout


class Knight(Player):
    CLASS_NAME = PlayerClasses.KNIGHT

    def __init__(self, name=None):
        super().__init__(name)
        self.name = name
        self.max_hp = 6000
        self.max_mana = 25
        self.hp = 6000
        self.mana = 25
        self.attack = Attack(10, 10, effects=self.effects)
        self.rest_hp = 15
        self.rest_mana = 5
        self.skills = SkillSet({
            "1": Berserker(),
            "2": BloodySlice(),
            "3": BattleShout(),
        })
