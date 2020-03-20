from effects.effects import FireShieldEffect
from skills.mage_skills import FireShield, Fireball, Lightining
from .player import Player
from skills.abstract_skills import SkillSet
from skills.attack_skill import Attack
from math import ceil


class Mage(Player):
    NAME = "Mag"

    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.max_hp = 40
        self.max_mana = 60
        self.hp = 40
        self.mana = 60
        self.attack = Attack(5, 5, effects=self.effects)
        self.rest_hp = 10
        self.rest_mana = 20
        self.skills = SkillSet({
            "1": Fireball(),
            "2": FireShield(),
            "3": Lightining(),
        })

    def take_dmg(self, attack) -> None:
        if self.effects.contains(FireShieldEffect):
            self.hp -= ceil(FireShieldEffect.DMG_RED * attack.dmg)
            return
        super().take_dmg(attack)

