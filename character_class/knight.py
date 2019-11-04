from character_class.player import Player
from random import randint


class Knight(Player):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.max_dmg = 15
        self.min_dmg = 10
        self.max_hp = 80
        self.max_mana = 20
        self.hp = 80
        self.mana = 20
        self.skills = [("Zwykły Atak", self.attack), ("Berserker", self.berserker), ]

    def berserker(self, other_player):
        if self.mana >= 15:
            self.mana -= 15
            other_player.hp -= randint(self.min_dmg, self.max_dmg) * 2
        else:
            print("\nBrakuje many\n")
            self.choose_skill(other_player)

    def battle_shout(self, other_player):
        if self.mana <= 5:
            self.min_dmg += 4
            self.max_dmg += 4
        else:
            print("\nBrakuje many\n")
            self.choose_skill(other_player)

    def rest(self):
        self.hp += 15
        self.mana += 5
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        if self.mana > self.max_mana:
            self.mana = self.max_mana
