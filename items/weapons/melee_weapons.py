from enums import PlayerClasses
from items.weapons.abstract_weapons import MeleeWeapon


class Scythe(MeleeWeapon):
    CRITICAL_STRIKE_CHANCE: int = 5
    NAME: str = "Kosa"
    WEARABLE_FOR: tuple = (
        PlayerClasses.MAGE,
        PlayerClasses.KNIGHT,
        PlayerClasses.PALADIN
    )

    def __init__(self) -> None:
        super().__init__()
        self.min_dmg: int = 5
        self.max_dmg: int = 5


class Cudgel(MeleeWeapon):
    CRITICAL_STRIKE_CHANCE: int = 5
    NAME: str = "Maczuga"
    WEARABLE_FOR: tuple = (
        PlayerClasses.MAGE,
        PlayerClasses.KNIGHT,
        PlayerClasses.PALADIN
    )

    def __init__(self) -> None:
        super().__init__()
        self.min_dmg: int = 7
        self.max_dmg: int = 10


class Axe(MeleeWeapon):
    CRITICAL_STRIKE_CHANCE: int = 7
    NAME: str = "Topór"
    WEARABLE_FOR: tuple = (
        PlayerClasses.MAGE,
        PlayerClasses.KNIGHT,
        PlayerClasses.PALADIN
    )

    def __init__(self) -> None:
        super().__init__()
        self.min_dmg: int = 10
        self.max_dmg: int = 12


class RustySword(MeleeWeapon):
    CRITICAL_STRIKE_CHANCE: int = 12
    NAME: str = "Zardzewiały miecz"
    WEARABLE_FOR: tuple = (
        PlayerClasses.MAGE,
        PlayerClasses.KNIGHT,
        PlayerClasses.PALADIN
    )

    def __init__(self) -> None:
        super().__init__()
        self.min_dmg: int = 12
        self.max_dmg: int = 15


class BattleAxe(MeleeWeapon):
    CRITICAL_STRIKE_CHANCE: int = 20
    NAME: str = "Topór bojowy"
    WEARABLE_FOR: tuple = (
        PlayerClasses.KNIGHT,
        PlayerClasses.PALADIN
    )

    def __init__(self) -> None:
        super().__init__()
        self.min_dmg: int = 20
        self.max_dmg: int = 30


class Inquisitor(MeleeWeapon):
    CRITICAL_STRIKE_CHANCE: int = 20
    NAME: str = "Inkwizytor"
    WEARABLE_FOR: tuple = (
        PlayerClasses.KNIGHT,
        PlayerClasses.PALADIN
    )

    def __init__(self) -> None:
        super().__init__()
        self.min_dmg: int = 35
        self.max_dmg: int = 40


class MasterSword(MeleeWeapon):
    CRITICAL_STRIKE_CHANCE: int = 25
    NAME: str = "Mistrzowski miecz"
    WEARABLE_FOR: tuple = (
        PlayerClasses.KNIGHT,
        PlayerClasses.PALADIN
    )

    def __init__(self) -> None:
        super().__init__()
        self.min_dmg: int = 40
        self.max_dmg: int = 60
