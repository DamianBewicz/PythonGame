from itertools import zip_longest


class PersonalItems:
    ITEMS = ["broń", "zbroja", "tarcza", "spodnie", "buty", "rękawice", "hełm"]

    def __init__(self) -> None:
        self.items = {item_type: None for item_type in PersonalItems.ITEMS}

    def __str__(self) -> str:
        string = ""
        for first_object, second_object in self.items.items():
            left = f'{str(first_object).capitalize()}'.split('\n')
            right = str(second_object).split('\n')
            right[-1] = right[-1] + "\n" if right[-1] != "None" else "Puste\n"
            for first_object_line, second_object_line in zip_longest(left, right, fillvalue=' ' * len(left[0])):
                string += "{:10}{}\n".format(first_object_line, second_object_line)
        return string

    def is_in_slot(self, item) -> bool:
        return self.items[item.SECTION.value.lower()] is not None

    def get_item(self, type):
        return self.items[type.lower()]

    def pop(self, type: str):
        item = self.items[type]
        self.items[type] = None
        return item

    def set(self, item) -> None:
        item_type = item.SECTION.value.lower()
        self.items[item_type] = item
