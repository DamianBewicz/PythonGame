from characters.player.level_up_stats import LevelUpStats
from characters.player.player import Player
from enums import PlayerClasses
from skills import Berserker, BloodySlice, BattleShout, Attack
from skills.abstract_skills import SkillSet


class Knight(Player):
    CLASS_NAME: PlayerClasses = PlayerClasses.KNIGHT

    def __init__(self, name: str = None) -> None:
        super().__init__(name)
        self.name: str = name
        self.max_hp: int = 60
        self.max_mana: int = 25
        self.hp: int = 60
        self.mana: int = 25
        self.rest_hp: int = 15
        self.rest_mana: int = 5
        self.level_up_stats = LevelUpStats(hp=30, mana=10)
        self.skills: SkillSet = SkillSet({
            "1": Berserker(),
            "2": BloodySlice(),
            "3": BattleShout(),
        })

    @property
    def attack(self) -> Attack:
        return Attack(10, 12, effects=self.effects) if self.equipment.personal_items.get_item("broń") is None else self.equipment.personal_items.get_item("broń")
