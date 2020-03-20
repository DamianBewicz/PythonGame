from effects.effects import BleedEffect, BattleShoutEffect
from skills.abstract_skills import Skill, Type, DmgDebuff, Buff
from random import randint


class Berserker(Skill):
    def __init__(self, mana_cost=15, min_dmg=20, max_dmg=30):
        super().__init__(mana_cost)
        self.type = Type.PHYSICAL
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg

    def __str__(self):
        return "Berserker"

    @property
    def dmg(self):
        return randint(self.min_dmg, self.max_dmg)

    def perform(self, character):
        character.take_dmg(self)


class BloodySlice(DmgDebuff):
    def __init__(self, mana_cost=10, min_dmg=10, max_dmg=15):
        super().__init__(mana_cost, min_dmg, max_dmg)
        self.type = Type.PHYSICAL
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg

    def __str__(self):
        return "Krawe Cięcie"

    @property
    def debuff(self):
        return BleedEffect()


class BattleShout(Buff):
    def __init__(self, mana_cost=10) -> None:
        super().__init__(mana_cost)

    def __str__(self) -> str:
        return "Okrzyk Bojowy"

    @property
    def buff(self):
        return BattleShoutEffect()

    def perform(self, character) -> None:
        if self.buff.is_activated():
            character.effects.append(self.buff)
