from characters import Enemy
from skills.attack_skill import Attack


class Orc(Enemy):
    def __init__(self, name="Goblin"):
        super().__init__(name)
        self.max_hp = 60
        self.max_mana = 0
        self.hp = 60
        self.mana = 0
        self.attack = Attack(5, 10)
        self.effects = []
        self.skills = [Revenge(), Fury()]
