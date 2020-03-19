from characters.player.player import Character


class Enemy(Character):

    def __init__(self, name: str):
        super().__init__(name)
        self.max_hp = NotImplemented
        self.max_mana = NotImplemented
        self.hp = NotImplemented
        self.mana = NotImplemented
        self.attack = NotImplemented
        self.effects = NotImplemented

    def perform_action(self, character):
        if not self.is_blinded:
            super().perform_action(character)

    def randomize_move(self):
        return NotImplemented