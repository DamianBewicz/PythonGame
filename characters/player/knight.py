from .player import Player
from skills.abstract_skills import SkillSet
from skills.attack_skill import Attack
from skills.knight_skills import Berserker, BloodySlice, BattleShout


class Knight(Player):
    def __init__(self, name=None):
        super().__init__(name)
        self.name = name
        self.max_hp = 60
        self.max_mana = 25
        self.hp = 60
        self.mana = 25
        self.attack = Attack(10, 20)
        self.rest_hp = 15
        self.rest_mana = 5
        self.effects = []
        self.skills = SkillSet({
            "1": Berserker(),
            "2": BloodySlice(),
            "3": BattleShout(),
        })

    def __str__(self):
        return "Rycerz"

    def remove_effect(self, effect):
        if effect.type == "DEBUFF STATS":
            self.attack.add(effect)
        if effect.type == "BUFF STATS":
            self.attack.sub(effect)
        self.effects.remove(effect)
