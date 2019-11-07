from items.health_potion import HealthPotion
from characters.character import Enemy


class Villager(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Wieśniak Władysław"
        self.max_dmg = 15
        self.min_dmg = 10
        self.max_hp = 30
        self.hp = 30
        self.gold_loot_range = 0, 20
        self.loot = [HealthPotion() for _ in range(11)]
