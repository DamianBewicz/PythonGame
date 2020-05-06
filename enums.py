from enum import Enum


class MagicNature(Enum):
    FIRE: str = "OGIEŃ"
    WATER: str = "WODA"
    EARTH: str = "ZIEMIA"
    LIGHTNING: str = "BŁYSKAWICA"
    SHADOW: str = "CIEŃ"


class AttackType(Enum):
    MAGIC: str = "MAGICZNY"
    PHYSICAL: str = "FIZYCZNY"
    NORMAL: str = "NORMALNY"
    HEAL: str = "LECZENIE"
    BUFF: str = "BUFF"
    DEBUFF: str = "DEBUFF"


class EquipmentSections(Enum):
    WEAPON: str = "BROŃ"
    HELMET: str = "HEŁM"
    ARMOR: str = "ZBROJA"
    TROUSERS: str = "SPODNIE"
    GLOVES: str = "RĘKAWICE"
    BOOTS: str = "BUTY"
    SHIELD: str = "TARCZA"


class ItemType(Enum):
    EQUIPPABLE: str = "WYPOSAŻENIE"


class PlayerClasses(Enum):
    KNIGHT: str = "RYCERZ"
    PALADIN: str = "PALADYN"
    MAGE: str = "CZARODZIEJ"
