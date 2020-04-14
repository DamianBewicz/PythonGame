from enum import Enum
from items.abstract_item import EquipableItem


class DefenseType(Enum):
    HELMET = "HEŁM"
    ARMOR = "ZBROJA"
    TROUSERS = "SPODNIE"
    GLOVES = "RĘKAWICE"
    BOOTS = "BUTY"
    SHIELD = "TARCZA"


class DefensiveItem(EquipableItem):
    SECTION = NotImplemented
    NAME = NotImplemented

    def __init__(self) -> None:
        self.defense = NotImplemented

    def __str__(self) -> str:
        return "{} - {} pkt pancerza".format(self.NAME, self.defense)


class Helmet(DefensiveItem):
    SECTION = DefenseType.HELMET


class Armor(DefensiveItem):
    SECTION = DefenseType.ARMOR


class Trousers(DefensiveItem):
    SECTION = DefenseType.TROUSERS


class Gloves(DefensiveItem):
    SECTION = DefenseType.GLOVES


class Boots(DefensiveItem):
    SECTION = DefenseType.BOOTS


class Shield(DefensiveItem):
    SECTION = DefenseType.SHIELD

    def __init__(self):
        super().__init__()
        self.percent_block_chance = NotImplemented
