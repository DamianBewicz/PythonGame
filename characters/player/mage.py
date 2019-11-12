from characters.enemies import Enemy
from .player import Player


class Mage(Player):
    NAME = "Mag"

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.name = name
        self.max_dmg = 7
        self.min_dmg = 5
        self.max_hp = 50
        self.max_mana = 40
        self.hp = 50
        self.mana = 40
        self.rest_hp_rate = 10
        self.rest_mana_rate = 15
        self.skills = [("Kula ognia", self.fireball), ]

    def fireball(self, enemy: Enemy) -> bool:
        if self.mana >= 20:
            enemy.hp -= 25
            return True
        print("\nBrakuje many\n")
        return False
