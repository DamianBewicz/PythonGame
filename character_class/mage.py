from character_class.player import Player


class Mage(Player):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.max_dmg = 7
        self.min_dmg = 5
        self.max_hp = 50
        self.max_mana = 40
        self.hp = 50
        self.mana = 40
        self.skills = [("Zwykły atak", self.attack), ("Kula ognia", self.fireball), ]

    def fireball(self, other_player):
        if self.mana <= 20:
            other_player.hp -= 25
            return True
        else:
            print("\nBrakuje many\n")
            return False
