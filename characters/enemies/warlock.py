from random import choices
from characters import Player
from characters.enemies.enemy import Enemy
from skills.attack_skill import Attack
from skills.warlock_skills import Curse


class Warlock(Enemy):
    def __init__(self, name: str = "Czarnoksiężnik") -> None:
        super().__init__(name)
        self.max_hp = 100
        self.max_mana = 200
        self.hp = 100
        self.mana = 200
        self.attack = Attack(5, 5, effects=self.effects)
        self.skills = [Curse()]
        self.pet = []

    def perform_action(self, character: Player) -> None:
        if not self.cant_move():
            move = self.randomize_move()[0]
            move.perform(character)

    def randomize_move(self) -> None:
        possible_moves = [self.attack]
        possible_moves.extend(self.skills)
        return choices(possible_moves, [80, 20])


# , Summon(), HealthDrain(), ManaDrain()