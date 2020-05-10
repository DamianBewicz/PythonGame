from characters.player.player import Player
from enums import PlayerClasses
from skills import Berserker, BloodySlice, BattleShout, Attack
from skills.abstract_skills import SkillSet


class Knight(Player):
    CLASS_NAME = PlayerClasses.KNIGHT

    def __init__(self, name=None):
        super().__init__(name)
        self.name = name
        self.max_hp = 6000
        self.max_mana = 2500
        self.hp = 6000
        self.mana = 2500
        self.rest_hp = 15
        self.rest_mana = 5
        self.skills = SkillSet({
            "1": Berserker(),
            "2": BloodySlice(),
            "3": BattleShout(),
        })

    @property
    def attack(self):
        return Attack(10, 12, effects=self.effects) if self.equipment.personal_items.get_item("broń") is None else self.equipment.personal_items.get_item("broń")
