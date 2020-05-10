from ..character import Character
from dmg_object.damage_object import DamageObject
from effects import EffectSet
from enums import AttackType


class Enemy(Character):
    def __init__(self, name: str):
        super().__init__(name)
        self.max_hp = NotImplemented
        self.max_mana = NotImplemented
        self.hp = NotImplemented
        self.mana = NotImplemented
        self.effects = EffectSet()

    def take_dmg(self, damage_object: DamageObject) -> None:
        self.hp -= damage_object.dmg

    def perform_action(self, character):
        if not self.cant_move():
            move = self.randomize_move()[0]
            if move.TYPE == AttackType.MAGIC or move.TYPE == AttackType.PHYSICAL:
                move.perform(character)
            else:
                move.perform(self)

    def randomize_move(self):
        return NotImplemented
