from enums import ItemType


class Item:
    TYPE = NotImplemented

    @staticmethod
    def get_item_type(item):
        return item.TYPE


class EquipableItem(Item):
    TYPE = ItemType.EQUIPPABLE
    NAME = NotImplemented
    SECTION = NotImplemented
    WEARABLE_FOR: tuple = NotImplemented

    @staticmethod
    def get_item_section(item) -> str:
        return item.SECTION.value.lower()

    def can_wear(self, player_class) -> bool:
        return player_class in self.WEARABLE_FOR
