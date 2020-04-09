from random import choices
from characters.enemies.enemy import Enemy
from skills.abstract_skills import Type
from skills.attack_skill import Attack
from skills.shaman_skills import EarthQuake, HealingRain


class Shaman(Enemy):
    def __init__(self, name="Szaman") -> None:
        super().__init__(name)
        self.max_hp = 100
        self.max_mana = 70
        self.hp = 100
        self.mana = 70
        self.attack = Attack(10, 10, effects=self.effects)
        self.skills = [HealingRain(), EarthQuake()]

    def heal(self, effect) -> None:
        self.hp += effect.hp
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def perform_action(self, character):
        if not self.cant_move():
            move = self.randomize_move()[0]
            if isinstance(move, Attack):
                move.perform(character)
            else:
                if self.has_mana(move):
                    if move.type == Type.MAGIC or move.type == Type.PHYSICAL:
                        move.perform(character)
                        self.lose_mana(move.mana_cost)
                    else:
                        if not self.has_full_hp():
                            move.perform(self)
                            self.lose_mana(move.mana_cost)
                        else:
                            self.attack.perform(character)

    def randomize_move(self):
        possible_moves = [self.attack]
        possible_moves.extend(self.skills)
        return choices(possible_moves, [60, 20, 20])

    def has_full_hp(self):
        return self.hp == self.max_hp
