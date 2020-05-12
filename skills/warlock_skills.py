from random import randint
from dmg_object.damage_object import DamageObject
from effects import CurseEffect
from enums import MagicNature
from pets import Imp
from skills.abstract_skills import Debuff, MagicDamageSkill, Skill


class Curse(Debuff):

    def __init__(self, mana_cost: int = 30) -> None:
        super().__init__(mana_cost)

    @property
    def effect(self) -> CurseEffect:
        return CurseEffect()


class HealthDrain(MagicDamageSkill):
    SOURCE = MagicNature.SHADOW

    def __init__(self, mana_cost: int = 30) -> None:
        super().__init__(mana_cost, min_dmg=500, max_dmg=500)

    @property
    def dmg(self) -> int:
        return randint(self.min_dmg, self.max_dmg)

    def perform(self, caster: 'Enemy', character: 'Player') -> None:
        dmg = self.dmg
        character.take_dmg(DamageObject(dmg=dmg, attack_type=self.TYPE, source=self.SOURCE))
        caster.heal(dmg)


class ManaDrain(MagicDamageSkill):
    SOURCE: MagicNature = MagicNature.SHADOW

    def __init__(self, mana_cost: int = 10, mana_drain: int = 30) -> None:
        super().__init__(mana_cost)
        self.mana_drain: int = mana_drain

    def perform(self, caster: 'Enemy', character: 'Player') -> None:
        character.take_dmg(DamageObject(dmg=self.mana_drain, attack_type=self.TYPE, source=self.SOURCE))
        caster.gain_mana(self.mana_drain)
        caster.lose_mana(self.mana_cost)


class SummonImp(Skill):

    def __init__(self, mana_cost: int = 60) -> None:
        super().__init__(mana_cost)

    @property
    def pet(self):
        return Imp()

    def perform(self, caster) -> None:
        caster.add_pet(self.pet)
