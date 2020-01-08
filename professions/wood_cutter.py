from random import randint
from items import MinorHealthPotion, MinorManaPotion


class WoodCutter:
    def __init__(self) -> None:
        self.gold_loot_range = 2, 10
        self.drop = [
            MinorHealthPotion(),
            MinorManaPotion(),
        ]
        self.item_drop_rate = [1, 1]

    def __str__(self) -> str:
        return "Pracuj jako pomocnik drwala"

    def get_pay(self, player) -> None:
        player.money += randint(*self.gold_loot_range)
        first_item_chance_draw = randint(1, 100)
        second_item_chance_draw = randint(1, 100)
        if first_item_chance_draw == self.item_drop_rate[0]:
            player.backpack.items.append(self.drop[0])
        elif second_item_chance_draw == self.item_drop_rate[1]:
            player.backpack.items.append(self.drop[1])
