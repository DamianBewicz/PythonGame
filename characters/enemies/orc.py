from random import choices
from characters.enemies.enemy import Enemy
from effects import Blind, FuryEffect
from skills import Fury, BloodySlice, Attack


class Orc(Enemy):
    def __init__(self, name="Ork"):
        super().__init__(name)
        self.max_hp = 60
        self.max_mana = 0
        self.hp = 60
        self.mana = 0
        self.skills = [Fury(), BloodySlice()]

    @property
    def attack(self):
        return Attack(20, 20, effects=self.effects)

    def perform_action(self, character):
        super().perform_action(character)
        if not self.effects.contains(Blind) and self.effects.contains(FuryEffect):
            self.attack.perform(character)

    def randomize_move(self):
        possible_moves = [self.attack]
        possible_moves.extend(self.skills)
        return choices(possible_moves, [70, 15, 15])
