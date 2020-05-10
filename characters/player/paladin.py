from characters.player.player import Player
from enums import PlayerClasses
from skills import HammerTime, HolyLight, HolyShield, Attack
from skills.abstract_skills import SkillSet


class Paladin(Player):
    CLASS_NAME = PlayerClasses.PALADIN

    def __init__(self, name) -> None:
        super().__init__(name)
        self.name = name
        self.max_hp = 5000
        self.max_mana = 35
        self.hp = 5000
        self.mana = 35
        self.rest_hp = 10
        self.rest_mana = 15
        self.skills = SkillSet({
            "1": HammerTime(),
            "2": HolyLight(),
            "3": HolyShield(),
        })

    @property
    def attack(self):
        return Attack(10, 12, effects=self.effects) if self.equipment.personal_items.get_item("broń") is None else self.equipment.personal_items.get_item("broń")
