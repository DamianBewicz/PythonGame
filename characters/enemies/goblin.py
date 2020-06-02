from random import choices
from characters.enemies.enemy import Enemy
from skills import SpearAttack, Attack


class Goblin(Enemy):
    def __init__(self, name: str = "Goblin") -> None:
        super().__init__(name)
        self.max_hp: int = 60
        self.max_mana: int = 0
        self.hp: int = 60
        self.mana: int = 0
        self.skills: list = [SpearAttack()]

    @property
    def attack(self) -> Attack:
        return Attack(10, 12, effects=self.effects)

    def perform_action(self, character) -> None:
        if not self.cant_move():
            move = self.randomize_move()[0]
            move.perform(character)

    def randomize_move(self):
        possible_moves = [self.attack]
        possible_moves.extend(self.skills)
        return choices(possible_moves, [80, 20])
