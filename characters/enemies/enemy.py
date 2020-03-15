from characters.player.player import Character
from skills.attack_skill import Attack


class Enemy(Character):
    def __init__(self, name: str):
        super().__init__(name)
        self.max_hp = 60
        self.max_mana = 25
        self.hp = 60
        self.mana = 25
        self.attack = Attack(5, 5)
        self.rest_hp = 15
        self.rest_mana = 5
        self.effects = []

    def perform_action(self, character):
        print(self.is_blinded())
        if not self.is_blinded:
            super().perform_action(character)
