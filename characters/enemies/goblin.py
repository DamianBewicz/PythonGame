from characters.enemies.enemy import Enemy
from skills.attack_skill import Attack
from skills.villager_skills import SpearAttack
from random import choices


class Goblin(Enemy):

    def __init__(self, name="Goblin"):
        super().__init__(name)
        self.max_hp = 60
        self.max_mana = 0
        self.hp = 60
        self.mana = 0
        self.attack = Attack(5, 10)
        self.effects = []
        self.skills = [SpearAttack()]

    def perform_action(self, character):
        if not self.is_blinded():
            move = self.randomize_move()[0]
            move.perform(character)

    def randomize_move(self):
        possible_moves = [self.attack]
        possible_moves.extend(self.skills)
        return choices(possible_moves, [80, 20])
