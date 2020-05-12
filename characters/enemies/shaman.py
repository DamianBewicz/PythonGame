from random import choices
from characters.enemies.enemy import Enemy
from enums import AttackType
from skills import HealingRain, EarthQuake, Attack


class Shaman(Enemy):
    def __init__(self, name: str = "Szaman") -> None:
        super().__init__(name)
        self.max_hp: int = 100
        self.max_mana: int = 70
        self.hp: int = 100
        self.mana: int = 70
        self.skills: list = [HealingRain(), EarthQuake()]

    @property
    def attack(self) -> Attack:
        return Attack(10, 12, effects=self.effects)

    def heal(self, effect) -> None:
        self.hp += effect.hp
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def perform_action(self, character) -> None:
        if not self.cant_move():
            move = self.randomize_move()[0]
            if type(move) == Attack:
                move.perform(character)
            else:
                if self.has_mana(move):
                    if move.TYPE == AttackType.MAGIC or move.TYPE == AttackType.PHYSICAL:
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

    def has_full_hp(self) -> bool:
        return self.hp == self.max_hp
