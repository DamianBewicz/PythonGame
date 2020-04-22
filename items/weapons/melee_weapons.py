from items.weapons.abstract_weapons import MeleeWeapon


class Scythe(MeleeWeapon):
    CRITICAL_STRIKE_CHANCE = 5
    NAME = "Kosa"

    def __init__(self) -> None:
        super().__init__()
        self.min_dmg = 5
        self.max_dmg = 5


class Cudgel(MeleeWeapon):
    CRITICAL_STRIKE_CHANCE = 5
    NAME = "Maczuga"

    def __init__(self) -> None:
        super().__init__()
        self.min_dmg = 7
        self.max_dmg = 10


class Axe(MeleeWeapon):
    CRITICAL_STRIKE_CHANCE = 7
    NAME = "Topór"

    def __init__(self) -> None:
        super().__init__()
        self.min_dmg = 10
        self.max_dmg = 12


class RustySword(MeleeWeapon):
    CRITICAL_STRIKE_CHANCE = 8
    NAME = "Zardzewiały miecz"

    def __init__(self) -> None:
        super().__init__()
        self.min_dmg = 12
        self.max_dmg = 15


class BattleAxe(MeleeWeapon):
    CRITICAL_STRIKE_CHANCE = 10
    NAME = "Topór bojowy"

    def __init__(self) -> None:
        super().__init__()
        self.min_dmg = 15
        self.max_dmg = 20


class Inquisitor(MeleeWeapon):
    CRITICAL_STRIKE_CHANCE = 15
    NAME = "Inkwizytor"

    def __init__(self) -> None:
        super().__init__()
        self.min_dmg = 25
        self.max_dmg = 30


class MasterSword(MeleeWeapon):
    CRITICAL_STRIKE_CHANCE = 25
    NAME = "Mistrzowski miecz"

    def __init__(self) -> None:
        super().__init__()
        self.min_dmg = 40
        self.max_dmg = 60
