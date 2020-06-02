from typing import Optional
from random import randint
from dmg_object.damage_object import DamageObject
from effects.abstract_effects import Effect
from enums import AttackType


class Skill:
    TYPE = NotImplemented

    def __init__(self, mana_cost: int = None) -> None:
        self.mana_cost: int = mana_cost


class DamageSkill(Skill):

    def __init__(self, mana_cost: int = None, min_dmg: int = None, max_dmg: int = None):
        super().__init__(mana_cost)
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg

    @property
    def dmg(self) -> int:
        return randint(self.min_dmg, self.max_dmg)


class PhysicalDamageSkill(DamageSkill):
    TYPE = AttackType.PHYSICAL


class MagicDamageSkill(DamageSkill):
    TYPE = AttackType.MAGIC
    SOURCE = NotImplemented


class AttackWithEffect(Skill):
    TYPE = NotImplemented

    @property
    def effect(self) -> Effect:
        return NotImplemented

    def perform(self, character) -> None:
        if self.effect.is_activated():
            character.effects.append(self.effect)


class Buff(AttackWithEffect):
    TYPE: str = AttackType.BUFF

    def __init__(self, mana_cost: int) -> None:
        super().__init__(mana_cost)

    def __str__(self) -> str:
        return NotImplemented


class Debuff(AttackWithEffect):
    TYPE: str = AttackType.DEBUFF

    def __init__(self, mana_cost: int) -> None:
        super().__init__(mana_cost)


class DmgDebuff(Debuff):
    ATTACK_TYPE = NotImplemented

    def __init__(self, mana_cost, min_dmg, max_dmg) -> None:
        super().__init__(mana_cost)
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg

    @property
    def dmg(self) -> int:
        return randint(self.min_dmg, self.max_dmg)

    def perform(self, character) -> None:
        super().perform(character)
        character.take_dmg(DamageObject(dmg=self.dmg, attack_type=self.ATTACK_TYPE))


class PhysicalDmgDebuff(DmgDebuff):
    ATTACK_TYPE = AttackType.PHYSICAL


class MagicDmgDebuff(DmgDebuff):
    ATTACK_TYPE = AttackType
    SOURCE = NotImplemented


class Heal(Skill):
    TYPE: str = AttackType.HEAL

    def __init__(self, mana_cost: int, hp: int) -> None:
        super().__init__(mana_cost)
        self.hp: int = hp

    def perform(self, character) -> None:
        character.heal(self.hp)


class SkillSet:
    def __init__(self, skills=None) -> None:
        self.skills = skills

    def introduce(self) -> None:
        for number, skill in self.skills.items():
            print(number, skill)

    def choose(self) -> Optional[Skill]:
        while True:
            self.introduce()
            choice = input("\nWybierz umiejętność, jeśli chcesz wyjść naciśnij enter\n")
            try:
                if choice == "":
                    return None
                return self.skills[choice]
            except KeyError:
                print("\nPodana wartość jest nieprawidłowa, proszę podać cyfrę!\n")
