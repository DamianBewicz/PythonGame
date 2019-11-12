from characters.enemies import Enemy
from items.potions import MinorHealthPotion


class Villager(Enemy):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Wieśniak Władysław"
        self.max_dmg = 15
        self.min_dmg = 10
        self.max_hp = 30
        self.hp = 30
        self.gold_loot_range = 0, 20
        self.loot = [MinorHealthPotion() for _ in range(11)]
