from characters.player.player import Character, Player
from effects.effects import CurseEffect
from pets.warlock_pet import Imp
from skills.abstract_skills import Debuff, Skill, Type


class Curse(Debuff):
    def __init__(self, mana_cost: int = 30) -> None:
        super().__init__(mana_cost)

    @property
    def debuff(self) -> CurseEffect:
        return CurseEffect()


class HealthDrain(Skill):
    def __init__(self, caster: Character, mana_cost: int = 30, hp: int = 15) -> None:
        super().__init__(mana_cost)
        self.caster = caster
        self.type = Type.MAGIC
        self.hp = hp

    @property
    def dmg(self):
        return self.hp

    def perform(self, character: Player) -> None:
        character.take_dmg(self.dmg)
        self.caster.heal(self.hp)


class ManaDrain(Skill):
    def __init__(self, caster: Character, mana_cost: int = 20, mana: int = 30) -> None:
        super().__init__(mana_cost)
        self.caster = caster
        self.type = Type.MAGIC
        self.mana = mana

    def perform(self, character: Player) -> None:
        character.take_dmg(self.mana)
        self.caster.gain_mana(self.mana)
        self.caster.lose_mana(self.mana_cost)


class SummonImp(Skill):
    def __init__(self, mana_cost: int = 60, caster: Character = None) -> None:
        super().__init__(mana_cost)
        self.caster = caster

    @property
    def pet(self):
        return Imp()

    def perform(self) -> None:
        self.caster.add_pet(self.pet)
