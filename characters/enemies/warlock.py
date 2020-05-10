from random import choices
from characters.enemies.enemy import Enemy
from characters.player.player import Player
from skills import Curse, HealthDrain, ManaDrain, SummonImp, Attack


class Warlock(Enemy):
    def __init__(self, name: str = "Czarnoksiężnik") -> None:
        super().__init__(name)
        self.max_hp = 100
        self.max_mana = 200
        self.hp = 100
        self.mana = 200
        self.skills = [Curse(), HealthDrain(), ManaDrain(), SummonImp()]
        self.pet = []

    @property
    def attack(self):
        return Attack(10, 12, effects=self.effects)

    def perform_action(self, character: Player) -> None:
        if not self.cant_move():
            if self.pet:
                self.pet[0].perform(character)
            move = self.randomize_move()[0]
            print(move)
            if type(move) == SummonImp:
                if not self.pet and self.has_mana(move):
                    move.perform(self)
                else:
                    self.attack.perform(character)
            elif type(move) == Attack:
                move.perform(character)
            else:
                if self.has_mana(move):
                    if type(move) in (HealthDrain, ManaDrain):
                        move.perform(self, character)
                    else:
                        move.perform(character)
                    self.lose_mana(move.mana_cost)
                else:
                    self.attack.perform(character)

    def randomize_move(self) -> None:
        possible_moves = [self.attack]
        possible_moves.extend(self.skills)
        return choices(possible_moves, [10, 15, 45, 15, 15])

    def add_pet(self, pet) -> None:
        self.pet.append(pet)
