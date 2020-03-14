from random import randint
from math import floor

from characters.player.abstract_classes import Character


class Enemy(Character):
    def __init__(self, name: str):
        super().__init__(name)
        self.max_hp = 60
        self.max_mana = 25
        self.hp = 60
        self.mana = 25
        self.attack = Attack(5, 5)
        self.rest_hp = 15
        self.rest_mana = 5
        self.effects = []