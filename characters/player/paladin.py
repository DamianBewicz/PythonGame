from characters.player.player import Player
from enums import PlayerClasses
from skills import HammerTime, HolyLight, HolyShield, Attack
from skills.abstract_skills import SkillSet


class Paladin(Player):
    CLASS_NAME: PlayerClasses = PlayerClasses.PALADIN

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.name: str = name
        self.max_hp: int = 5000
        self.max_mana: int = 35
        self.hp: int = 5000
        self.mana: int = 35
        self.rest_hp: int = 10
        self.rest_mana: int = 15
        self.skills: SkillSet = SkillSet({
            "1": HammerTime(),
            "2": HolyLight(),
            "3": HolyShield(),
        })

    @property
    def attack(self) -> Attack:
        return Attack(10, 12, effects=self.effects) if self.equipment.personal_items.get_item("broń") is None else self.equipment.personal_items.get_item("broń")
