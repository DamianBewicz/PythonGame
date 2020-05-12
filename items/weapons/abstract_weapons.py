from random import randint
from dmg_object.damage_object import DamageObject
from enums import AttackType, EquipmentSections, MagicNature, PlayerClasses
from items.abstract_item import EquipableItem


class BonusDamage:
    def __init__(self, min_dmg: int, max_dmg: int):
        self.min_dmg: int = min_dmg
        self.max_dmg: int = max_dmg


class Weapon(EquipableItem):
    SECTION: EquipmentSections = EquipmentSections.WEAPON
    ATTACK_TYPE: AttackType = NotImplemented
    CRITICAL_STRIKE_CHANCE: int = NotImplemented
    BONUS_DMG: BonusDamage = NotImplemented

    def __init__(self) -> None:
        self.min_dmg: int = NotImplemented
        self.max_dmg: int = NotImplemented
        self.is_improved: bool = False

    def __str__(self) -> str:
        return "{}\n" \
               "Obrażenia {}-{}\n" \
               "Szansa na trafienie krytyczne {} %".format(self.NAME, self.min_dmg, self.max_dmg, self.CRITICAL_STRIKE_CHANCE)

    @property
    def damage(self) -> int:
        damage_multiplier = 1
        if self._critically_strikes:
            damage_multiplier = 2
        total_dmg = damage_multiplier * randint(self.min_dmg, self.max_dmg)
        print(total_dmg)
        return total_dmg

    @property
    def _critically_strikes(self) -> bool:
        return randint(1, 100) in range(1, self.CRITICAL_STRIKE_CHANCE + 1)

    def perform(self, character) -> None:
        return NotImplemented

    def improve(self) -> None:
        return NotImplemented


class MeleeWeapon(Weapon):
    ATTACK_TYPE: AttackType = AttackType.PHYSICAL
    BONUS_DMG: BonusDamage = BonusDamage(5, 5)

    def __init__(self) -> None:
        super().__init__()
        self.is_sharpened: bool = False

    def improve(self) -> None:
        self.min_dmg += self.BONUS_DMG.min_dmg
        self.max_dmg += self.BONUS_DMG.max_dmg
        self.is_improved = True

    def perform(self, character) -> None:
        character.take_dmg(DamageObject(dmg=self.damage, attack_type=self.ATTACK_TYPE))


class Wand(Weapon):
    ATTACK_TYPE: AttackType = AttackType.MAGIC
    NATURE: MagicNature = NotImplemented
    MAX_LEVEL: int = 4
    WEARABLE_FOR: tuple = (
        PlayerClasses.MAGE,
    )

    def __init__(self) -> None:
        super().__init__()
        self.level: int = 1

    def improve(self) -> None:
        self.min_dmg += self.BONUS_DMG.min_dmg
        self.max_dmg += self.BONUS_DMG.max_dmg
        self.level += 1
        if self.is_maximum_level():
            self.is_improved = True

    def is_maximum_level(self) -> bool:
        return self.MAX_LEVEL == self.level

    def perform(self, character) -> None:
        character.take_dmg(DamageObject(dmg=self.damage, attack_type=self.ATTACK_TYPE, source=self.NATURE))
