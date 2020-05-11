from random import choices
from characters.enemies.enemy import Enemy
from skills import SpearAttack, Attack


class Goblin(Enemy):
    def __init__(self, name="Goblin"):
        super().__init__(name)
        self.max_hp = 6000
        self.max_mana = 0
        self.hp = 6000
        self.mana = 0
        self.skills = [SpearAttack()]

    @property
    def attack(self):
        return Attack(10, 12, effects=self.effects)

    def perform_action(self, character):
        if not self.cant_move():
            move = self.randomize_move()[0]
            move.perform(character)

    def randomize_move(self):
        possible_moves = [self.attack]
        possible_moves.extend(self.skills)
        return choices(possible_moves, [10, 90])
