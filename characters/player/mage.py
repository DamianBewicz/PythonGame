from characters.player.player import Player
from effects import FireShieldEffect
from enums import PlayerClasses
from math import ceil
from skills import Attack, Fireball, FireShield, Lightining
from skills.abstract_skills import SkillSet


class Mage(Player):
    CLASS_NAME = PlayerClasses.MAGE

    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.max_hp = 4000
        self.max_mana = 6000
        self.hp = 4000
        self.mana = 6000
        self.rest_hp = 10
        self.rest_mana = 20
        self.skills = SkillSet({
            "1": Fireball(),
            "2": FireShield(),
            "3": Lightining(),
        })

    @property
    def attack(self):
        return Attack(10, 12, effects=self.effects) if self.equipment.personal_items.get_item("broń") is None else self.equipment.personal_items.get_item("broń")

    def take_dmg(self, damage_object) -> None:
        if self.effects.contains(FireShieldEffect):
            self.hp -= ceil(FireShieldEffect.DMG_RED * damage_object.dmg)
            return
        super().take_dmg(damage_object)
