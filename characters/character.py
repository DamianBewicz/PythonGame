from random import randint


class Enemy:
    def __init__(self):
        self.name = None
        self.max_dmg = None
        self.min_dmg = None
        self.hp = None
        self.gold_loot_range = None, None
        self.items = []

    def __str__(self):
        return f"""\n{self.name}
Punkty życia : {self.hp}\n"""

    def attack(self, other_player):
        other_player.hp -= randint(self.min_dmg, self.max_dmg)

    def is_dead(self):
        return self.hp <= 0

    def drop(self, other_player):
        if self.is_dead():
            other_player.money += randint(self.gold_loot_range[0], self.gold_loot_range[1])