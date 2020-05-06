from items.weapons import WandOfFire, WandOfWater, WandOfEarth, WandOfLightning, WandOfShadow
from items.weapons.abstract_weapons import Wand
from merchants.merchant import WeaponImprover


class Enchanter(WeaponImprover):
    IMPROVE_PRICE: int = 50
    WEAPON_FOR_IMPROVING = Wand
    QUESTION = "\nPodaj numer przedmiotu, który chcesz naostrzyć, lub naciśnij enter aby wyjść\n"


class AmateurEnchanter(Enchanter):
    ITEMS_PRICES: dict = {
        WandOfFire: 100,
        WandOfWater: 100,
        WandOfEarth: 100,
        WandOfLightning: 100,
        WandOfShadow: 100,
    }
    MARGIN: float = 0.5
