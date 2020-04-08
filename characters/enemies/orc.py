from random import choices
from characters.enemies.enemy import Enemy
from effects.effects import FuryEffect, Blind
from skills.attack_skill import Attack
from skills.knight_skills import BloodySlice
from skills.orc_skills import Fury


class Orc(Enemy):
    def __init__(self, name="Ork"):
        super().__init__(name)
        self.max_hp = 60
        self.max_mana = 0
        self.hp = 60
        self.mana = 0
        self.attack = Attack(10, 10, effects=self.effects)
        self.skills = [Fury(), BloodySlice()]

    def perform_action(self, character):
        super().perform_action(character)
        if not self.effects.contains(Blind) and self.effects.contains(FuryEffect):
            self.attack.perform(character)

    def randomize_move(self):
        possible_moves = [self.attack]
        possible_moves.extend(self.skills)
        return choices(possible_moves, [70, 15, 15])
