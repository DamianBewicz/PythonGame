from characters.player.player import Character, Player
from effects.effects import CurseEffect
from skills.abstract_skills import Debuff, Skill, Type


class Curse(Debuff):
    def __init__(self, mana_cost=30) -> None:
        super().__init__(mana_cost)

    @property
    def debuff(self) -> CurseEffect:
        return CurseEffect()


class HealthDrain(Skill):
    def __init__(self, hp: int, caster: Character, mana_cost: int = 30) -> None:
        super().__init__(mana_cost)
        self.caster = caster
        self.type = Type.MAGIC
        self.hp = hp

    def perform(self, character: Player) -> None:
        character.take_dmg(self.hp)
        self.caster.heal(self.hp)


class ManaDrain(Skill):
    def __init__(self, mana: int, caster: Character, mana_cost: int = 30) -> None:
        super().__init__(mana_cost)
        self.caster = caster
        self.type = Type.MAGIC
        self.mana = mana

    def perform(self, character: Player) -> None:
        character.take_dmg(self.mana)
        self.caster.gain_mana(self.mana)
