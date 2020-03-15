from effects.effectv import FireShieldEffect
from skills.mage_skills import FireShield, Fireball, Lightining
from .player import Player
from skills.abstract_skills import SkillSet, Type
from skills.attack_skill import Attack
from math import ceil


class Mage(Player):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.max_hp = 40
        self.max_mana = 60
        self.hp = 40
        self.mana = 60
        self.attack = Attack(5, 5)
        self.rest_hp = 10
        self.rest_mana = 20
        self.effects = []
        self.skills = SkillSet({
            "1": Fireball(),
            "2": FireShield(),
            "3": Lightining(),
        })

    def __str__(self):
        return "Mag"

    def take_dmg(self, attack) -> None:
        for e in self.effects:
            if isinstance(e, FireShieldEffect):
                self.hp -= ceil(FireShieldEffect.DMG_RED * attack.dmg)
                return
        super().take_dmg(attack)

