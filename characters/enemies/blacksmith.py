from characters.enemies.enemy import Enemy
from items import MinorHealthPotion
from random import randint


class Blacksmith(Enemy):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Zygmunt Kowal"
        self.max_hp = 45
        self.max_mana = 20
        self.hp = 45
        self.mana = 20
        self.max_dmg = 20
        self.min_dmg = 10
        self.gold_loot_range = 30, 50
        self.loot = [MinorHealthPotion()]
        self.skills.append(self.hammer_punch)

    def hammer_punch(self, character) -> None:
        print("Czas młota!")
        character.hp -= round(randint(self.min_dmg, self.max_dmg) * 1.4)
