from random import choices
from characters import Player
from characters.enemies.enemy import Enemy
from skills.attack_skill import Attack
from skills.warlock_skills import Curse, HealthDrain, ManaDrain, SummonImp


class Warlock(Enemy):
    def __init__(self, name: str = "Czarnoksiężnik") -> None:
        super().__init__(name)
        self.max_hp = 100
        self.max_mana = 200
        self.hp = 100
        self.mana = 200
        self.attack = Attack(5, 5, effects=self.effects)
        self.skills = [Curse(), HealthDrain(caster=self), ManaDrain(caster=self), SummonImp(caster=self)]
        self.pet = []

    def perform_action(self, character: Player) -> None:
        if not self.cant_move():
            if self.pet:
                self.pet[0].perform(character)
            move = self.randomize_move()[0]
            print(move)
            if type(move) == SummonImp:
                if not self.pet:
                    move.perform()
                else:
                    self.attack.perform(character)
            elif type(move) == Attack:
                move.perform(character)
            else:
                if self.has_mana(move):
                    move.perform(character)

    def randomize_move(self) -> None:
        possible_moves = [self.attack]
        possible_moves.extend(self.skills)
        return choices(possible_moves, [40, 15, 15, 5, 25])

    def add_pet(self, pet) -> None:
        self.pet.append(pet)
