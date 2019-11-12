from characters.enemies.enemy import Enemy
from items import MinorHealthPotion


class Blacksmith(Enemy):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Zygmunt Kowal"
        self.max_hp = 45
        self.hp = 45
        self.max_dmg = 20
        self.min_dmg = 10
        self.gold_loot_range = 30, 50
        self.loot = [MinorHealthPotion()]
