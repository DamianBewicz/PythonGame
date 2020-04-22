from items.weapons.abstract_weapons import MeleeWeapon
from merchants.merchant import Merchant
from utils import choose_item, introduce_from_list


class Blacksmith(Merchant):
    ITEMS_PRICES: dict = {

    }
    MARGIN: float = 0.5
    SHARPEN_PRICE: int = 30
    WEAPONS_FOR_SHARPENING = MeleeWeapon

    def _has_money_for_sharpen(self, player) -> bool:
        return player.equipment.gold.ammount >= self.SHARPEN_PRICE

    def _can_sharpen(self, player, item) -> bool:
        return self._has_money_for_sharpen(player) and isinstance(item, self.WEAPONS_FOR_SHARPENING) and not item.is_sharpened

    def sharpen_weapon(self, player) -> None:
        while True:
            players_backpack_items = player.equipment.backpack.items
            question = "\nPodaj numer przedmiotu, który chcesz naostrzyć, lub naciśnij enter aby wyjść\n"
            introduce_from_list(players_backpack_items)
            print("\nKoszt ulepszenia broni " + str(self.SHARPEN_PRICE) + "\n")
            chosen_item = choose_item(players_backpack_items, question)
            if chosen_item is not None:
                if self._can_sharpen(player, chosen_item):
                    player.equipment.gold.subtract(self.SHARPEN_PRICE)
                    chosen_item.sharpen()
                else:
                    print("\nNie można naostrzyć broni\n")
            else:
                break
