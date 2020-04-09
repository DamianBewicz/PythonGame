from characters.player.player import Character
from effects.effects_set import EffectSet
from skills.abstract_skills import Type


class Enemy(Character):

    def __init__(self, name: str):
        super().__init__(name)
        self.max_hp = NotImplemented
        self.max_mana = NotImplemented
        self.hp = NotImplemented
        self.mana = NotImplemented
        self.attack = NotImplemented
        self.effects = EffectSet()

    def perform_action(self, character):
        if not self.cant_move():
            move = self.randomize_move()[0]
            if move.type == Type.MAGIC or move.type == Type.PHYSICAL:
                move.perform(character)
            else:
                move.perform(self)

    def randomize_move(self):
        return NotImplemented
