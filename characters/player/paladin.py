from .player import Player
from skills.abstract_skills import SkillSet
from skills.attack_skill import Attack
from skills.paladin_skills import HammerTime, HolyLight, HolyShield


class Paladin(Player):
    NAME = "Paladyn"

    def __init__(self, name) -> None:
        super().__init__(name)
        self.name = name
        self.max_hp = 5000
        self.max_mana = 35
        self.hp = 5000
        self.mana = 35
        self.attack = Attack(5, 15, effects=self.effects)
        self.rest_hp = 10
        self.rest_mana = 15
        self.skills = SkillSet({
            "1": HammerTime(),
            "2": HolyLight(),
            "3": HolyShield(),
        })
