class PersonalItems:
    ITEMS = ["broń", "zbroja", "tarcza", "spodnie", "buty", "rękawice", "hełm"]

    def __init__(self) -> None:
        self.items = {item_type: None for item_type in PersonalItems.ITEMS}

    def __str__(self) -> str:
        all_items = ""
        for category, item in self.items.items():
            all_items += "{category:10}: {item}\n".format(
                category=category.capitalize(),
                item=item or "Puste"
            )
        return all_items

    @staticmethod
    def get_total(equipment, category: str) -> int:
        value = 0
        for item in PersonalItems.ITEMS:
            try:
                value += getattr(equipment, item).defense if category == "defense" else getattr(equipment, item).attack
            except AttributeError:
                pass
        return value

    def is_in_slot(self, item) -> bool:
        return self.items[item.SECTION.value.lower()] is not None

    def pop(self, type: str):
        item = self.items[type]
        self.items[type] = None
        return item

    def set(self, item) -> None:
        item_type = item.SECTION.value.lower()
        self.items[item_type] = item
