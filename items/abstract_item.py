from enum import Enum


class ItemType(Enum):
    EQUIPABLE = "EQUIPABLE"


class Item:
    TYPE = NotImplemented

    def use(self):
        return NotImplemented

    @staticmethod
    def get_item_type(item):
        return item.TYPE.value.lower()


class EquipableItem(Item):
    TYPE = ItemType.EQUIPABLE

    @staticmethod
    def get_item_section(item):
        return item.SECTION.value.lower()
