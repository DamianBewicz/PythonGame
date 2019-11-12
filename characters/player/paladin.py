from .player import Player


class Paladin(Player):
    NAME = "Paladyn"

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.name = name
        self.max_dmg = 12
        self.min_dmg = 8
        self.max_hp = 70
        self.max_mana = 30
        self.hp = 70
        self.mana = 30
        self.rest_hp_rate = 15
        self.rest_mana_rate = 10
        self.skills = [
            ("Święty Blask", self.holy_light),
            ("Błogosławiony Młot", self.blessed_hammer),
        ]

    def holy_light(self) -> bool:
        # Returns True if action was corectly performed,otherwise returns False.
        if self.mana <= 10:
            self.hp += 20
            return True
        print("\nBrakuje many\n")
        return False

    def blessed_hammer(self) -> bool:
        # Returns True if action was corectly performed,otherwise returns False.
        if self.mana <= 25:
            self.min_dmg += 15
            self.max_dmg += 15
            return True
        print("\nBrakuje many\n")
        return False
