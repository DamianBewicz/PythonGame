from enums import ItemType, EquipmentSections


class Item:
    TYPE: ItemType = NotImplemented

    @staticmethod
    def get_item_type(item):
        return item.STATUS_EFFECT


class EquipableItem(Item):
    TYPE: ItemType = ItemType.EQUIPPABLE
    NAME: str = NotImplemented
    SECTION: EquipmentSections = NotImplemented
    WEARABLE_FOR: tuple = NotImplemented

    @staticmethod
    def get_item_section(item) -> str:
        return item.SECTION.value.lower()

    def can_wear(self, player_class) -> bool:
        return player_class in self.WEARABLE_FOR


class Potion:
    TYPE: str = ItemType.POTION
    NAME: str = NotImplemented
