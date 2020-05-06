from random import randint
from enums import EquipmentSections
from items.abstract_item import EquipableItem


class DefensiveItem(EquipableItem):
    SECTION = NotImplemented
    RESISTANCE = NotImplemented
    STARTING_DEFENSE = NotImplemented

    def __init__(self) -> None:
        self.defense = self.STARTING_DEFENSE

    def __str__(self) -> str:
        return "{}\n" \
               "{}".format(self.NAME, str(self.defense))


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

    def __init__(self) -> None:
        super().__init__()

    def has_blocked(self) -> bool:
        return randint(1, 100) in range(1, self.BLOCK_CHANCE + 1)
