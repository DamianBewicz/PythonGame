from characters.character import Enemy


class Blacksmith(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Zygmunt Kowal"
        self.max_hp = 45
        self.hp = 45
        self.max_dmg = 20
        self.min_dmg = 10
