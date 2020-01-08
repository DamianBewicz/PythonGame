from characters.player.player import Player
from effects.effect import Effect
from collections import namedtuple

dmg_boost = namedtuple("dmg_boost", ("min_dmg", "max_dmg"))


class HolyHammer(Effect):
    def __init__(self) -> None:
        super().__init__()
        self.type = "Static"
        self.duration = 3
        self.effect_chance = 100
        self.dmg_buff = dmg_boost(5, 10)

    def __str__(self) -> str:
        return "\nCzas młota!\n"

    def perform_action(self, character: Player) -> None:
        print(self)
        character.min_dmg += self.dmg_buff.min_dmg
        character.max_dmg += self.dmg_buff.max_dmg

    def remove_buff(self, character) -> None:
        character.min_dmg -= self.dmg_buff.min_dmg
        character.max_dmg -= self.dmg_buff.max_dmg
