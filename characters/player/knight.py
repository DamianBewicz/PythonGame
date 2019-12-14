from typing import Type
from random import randint
from effects.bleed import Bleed
from ..enemies import Enemy
from .player import Player


class Knight(Player):
    NAME = "Rycerz"

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.name = name
        self.max_dmg = 15
        self.min_dmg = 10
        self.max_hp = 80
        self.max_mana = 20
        self.hp = 80
        self.mana = 20
        self.rest_hp_rate = 20
        self.rest_mana_rate = 5
        self.skills = [
            ("Berserker", self.berserker),
            ("Krwawe cięcie", self.bloody_slice),
            ("Okrzyk bojowy", self.battle_shout),
        ]

    def berserker(self, enemy: Enemy) -> bool:
        # Returns True if action was corectly performed,otherwise returns False.
        if self.mana >= 15:
            self.mana -= 15
            enemy.hp -= randint(self.min_dmg, self.max_dmg) * 2
            return True
        print("\nBrakuje many\n")
        return False

    def bloody_slice(self, enemy: Enemy):
        if self.mana >= 10:
            bleed = Bleed()
            enemy.hp -= randint(self.min_dmg, self.max_dmg)
            bleed.add_effect(enemy)
            return True
        print("\nBrakuje many\n")
        return False

    def battle_shout(self) -> bool:
        # Returns True if action was corectly performed,otherwise returns False.
        if self.mana >= 5:
            self.min_dmg += 4
            self.max_dmg += 4
            return True
        print("\nBrakuje many\n")
        return False

