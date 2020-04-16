from enums import MagicNature
from items.weapons.abstract_weapons import Wand, BonusDamage
from termcolor import colored


class WandOfFire(Wand):
    NATURE: MagicNature = MagicNature.FIRE
    CRITICAL_STRIKE_CHANCE: int = 20
    NAME: str = colored("Różdzka ognia", "red")
    BONUS_DMG: BonusDamage = BonusDamage(5, 10)

    def __init__(self) -> None:
        super().__init__()
        self.min_dmg: int = 15
        self.max_dmg: int = 30


class WandOfWater(Wand):
    NATURE: MagicNature = MagicNature.WATER
    CRITICAL_STRIKE_CHANCE: int = 20
    NAME: str = colored("Różdzka wody", "blue")
    BONUS_DMG: BonusDamage = BonusDamage(5, 10)

    def __init__(self) -> None:
        super().__init__()
        self.min_dmg = 10
        self.max_dmg = 25


class WandOfEarth(Wand):
    NATURE = MagicNature.EARTH
    CRITICAL_STRIKE_CHANCE = 25
    NAME = colored("Różdzka ziemi", "yellow")
    BONUS_DMG: BonusDamage = BonusDamage(5, 10)

    def __init__(self) -> None:
        super().__init__()
        self.min_dmg: int = 20
        self.max_dmg: int = 30


class WandOfLightning(Wand):
    NATURE: MagicNature = MagicNature.LIGHTNING
    CRITICAL_STRIKE_CHANCE: int = 15
    NAME: str = colored("Różdzka błyskawic", "grey")
    BONUS_DMG: BonusDamage = BonusDamage(10, 10)

    def __init__(self) -> None:
        super().__init__()
        self.min_dmg: int = 15
        self.max_dmg: int = 25


class WandOfShadow(Wand):
    NATURE: MagicNature = MagicNature.SHADOW
    CRITICAL_STRIKE_CHANCE: int = 10
    NAME: str = colored("Różdzka cienia", "white")
    BONUS_DMG: BonusDamage = BonusDamage(15, 15)

    def __init__(self) -> None:
        super().__init__()
        self.min_dmg: int = 15
        self.max_dmg: int = 20
