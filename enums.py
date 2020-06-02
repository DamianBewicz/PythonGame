from enum import Enum


class MagicNature(Enum):
    FIRE = "OGIEŃ"
    WATER = "WODA"
    EARTH = "ZIEMIA"
    LIGHTNING = "BŁYSKAWICA"
    SHADOW = "CIEŃ"


class AttackType(Enum):
    MAGIC = "MAGICZNY"
    PHYSICAL = "FIZYCZNY"
    NORMAL = "NORMALNY"
    HEAL = "LECZENIE"
    BUFF = "BUFF"
    DEBUFF = "DEBUFF"


class EquipmentSections(Enum):
    WEAPON = "BROŃ"
    HELMET = "HEŁM"
    ARMOR = "ZBROJA"
    TROUSERS = "SPODNIE"
    GLOVES = "RĘKAWICE"
    BOOTS = "BUTY"
    SHIELD = "TARCZA"


class ItemType(Enum):
    EQUIPPABLE = "WYPOSAŻENIE"
    POTION = "MIKSTURA"


class PlayerClasses(Enum):
    KNIGHT = "RYCERZ"
    PALADIN = "PALADYN"
    MAGE = "CZARODZIEJ"
