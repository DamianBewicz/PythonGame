from random import randint
from enums import AttackType, EquipmentSections, MagicNature
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

    def __str__(self) -> str:
        return NotImplemented

    @property
    def damage(self) -> int:
        damage_multiplier = 1
        if self._critically_strikes:
            damage_multiplier = 2
        return damage_multiplier * randint(self.min_dmg, self.max_dmg)

    @property
    def _critically_strikes(self) -> bool:
        return randint(1, 100) in range(1, self.CRITICAL_STRIKE_CHANCE + 1)


class MeleeWeapon(Weapon):
    ATTACK_TYPE: AttackType = AttackType.PHYSICAL
    BONUS_DMG: BonusDamage = BonusDamage(5, 5)

    def __init__(self) -> None:
        super().__init__()
        self.is_sharpened = False

    def __str__(self) -> str:
        return "{}\n" \
               "Obrażenia {} - {}\n" \
               "Szansa na trafienie krytyczne {}%".format(self.NAME, self.min_dmg, self.max_dmg, self.CRITICAL_STRIKE_CHANCE)

    def sharpen(self) -> None:
        self.min_dmg += self.BONUS_DMG.min_dmg
        self.max_dmg += self.BONUS_DMG.max_dmg
        self.is_sharpened = True


class Wand(Weapon):
    ATTACK_TYPE: AttackType = AttackType.MAGIC
    NATURE: MagicNature = NotImplemented
    MAX_LEVEL: int = 4

    def __init__(self) -> None:
        super().__init__()
        self.level: int = 1

    def __str__(self) -> str:
        return "{} - obrażenia {}-{}".format(self.NAME, self.min_dmg, self.max_dmg)

    def upgrade(self) -> None:
        self.min_dmg += self.BONUS_DMG.min_dmg
        self.max_dmg += self.BONUS_DMG.max_dmg
        self.level += 1

    def is_maximum_level(self) -> bool:
        return self.MAX_LEVEL == self.level
