from enums import PlayerClasses
from items.weapons.abstract_weapons import MeleeWeapon


class Scythe(MeleeWeapon):
    CRITICAL_STRIKE_CHANCE = 5
    NAME = "Kosa"
    WEARABLE_FOR: tuple = (
        PlayerClasses.MAGE,
        PlayerClasses.KNIGHT,
        PlayerClasses.PALADIN
    )

    def __init__(self) -> None:
        super().__init__()
        self.min_dmg = 5
        self.max_dmg = 5


class Cudgel(MeleeWeapon):
    CRITICAL_STRIKE_CHANCE = 5
    NAME = "Maczuga"
    WEARABLE_FOR: tuple = (
        PlayerClasses.MAGE,
        PlayerClasses.KNIGHT,
        PlayerClasses.PALADIN
    )

    def __init__(self) -> None:
        super().__init__()
        self.min_dmg = 7
        self.max_dmg = 10


class Axe(MeleeWeapon):
    CRITICAL_STRIKE_CHANCE = 7
    NAME = "Topór"
    WEARABLE_FOR: tuple = (
        PlayerClasses.MAGE,
        PlayerClasses.KNIGHT,
        PlayerClasses.PALADIN
    )

    def __init__(self) -> None:
        super().__init__()
        self.min_dmg = 10
        self.max_dmg = 12


class RustySword(MeleeWeapon):
    CRITICAL_STRIKE_CHANCE = 12
    NAME = "Zardzewiały miecz"
    WEARABLE_FOR: tuple = (
        PlayerClasses.MAGE,
        PlayerClasses.KNIGHT,
        PlayerClasses.PALADIN
    )

    def __init__(self) -> None:
        super().__init__()
        self.min_dmg = 12
        self.max_dmg = 15


class BattleAxe(MeleeWeapon):
    CRITICAL_STRIKE_CHANCE = 20
    NAME = "Topór bojowy"
    WEARABLE_FOR: tuple = (
        PlayerClasses.KNIGHT,
        PlayerClasses.PALADIN
    )

    def __init__(self) -> None:
        super().__init__()
        self.min_dmg = 20
        self.max_dmg = 30


class Inquisitor(MeleeWeapon):
    CRITICAL_STRIKE_CHANCE = 20
    NAME = "Inkwizytor"
    WEARABLE_FOR: tuple = (
        PlayerClasses.KNIGHT,
        PlayerClasses.PALADIN
    )

    def __init__(self) -> None:
        super().__init__()
        self.min_dmg = 35
        self.max_dmg = 40


class MasterSword(MeleeWeapon):
    CRITICAL_STRIKE_CHANCE = 25
    NAME = "Mistrzowski miecz"
    WEARABLE_FOR: tuple = (
        PlayerClasses.KNIGHT,
        PlayerClasses.PALADIN
    )

    def __init__(self) -> None:
        super().__init__()
        self.min_dmg = 40
        self.max_dmg = 60
