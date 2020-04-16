from enums import EquipmentSections
from items.abstract_item import EquipableItem


class DefensiveItem(EquipableItem):
    SECTION = NotImplemented
    RESISTANCE = NotImplemented

    def __init__(self) -> None:
        self.defense = NotImplemented

    def __str__(self) -> str:
        return "{} - {} pkt pancerza".format(self.NAME, self.defense)


class Helmet(DefensiveItem):
    SECTION = EquipmentSections.HELMET


class Armor(DefensiveItem):
    SECTION = EquipmentSections.ARMOR


class Trousers(DefensiveItem):
    SECTION = EquipmentSections.TROUSERS


class Gloves(DefensiveItem):
    SECTION = EquipmentSections.GLOVES


class Boots(DefensiveItem):
    SECTION = EquipmentSections.BOOTS


class Shield(DefensiveItem):
    SECTION = EquipmentSections.SHIELD
    BLOCK_CHANCE = NotImplemented

    def __init__(self):
        super().__init__()
