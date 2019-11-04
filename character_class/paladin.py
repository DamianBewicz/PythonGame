from character_class.player import Player


class Paladin(Player):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.max_dmg = 12
        self.min_dmg = 8
        self.max_hp = 70
        self.max_mana = 30
        self.hp = 70
        self.mana = 30
        self.skills = [("Święty Blask", self.holy_light), ("Błogosławiony Młot", self.blessed_hammer)]

    def holy_light(self):
        if self.mana <= 10:
            self.hp += 20
        else:
            print("\nBrakuje many\n")

    def blessed_hammer(self):
        if self.mana <= 25:
            self.min_dmg += 15
            self.max_dmg += 15
        else:
            print("\nBrakuje many\n")
