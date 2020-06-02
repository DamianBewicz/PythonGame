from items import WandOfFire, WandOfWater, WandOfEarth, WandOfLightning, WandOfShadow
from items.weapons.abstract_weapons import Wand
from merchants.merchant import WeaponImprover


class Enchanter(WeaponImprover):
    IMPROVE_PRICE: int = 50
    WEAPON_FOR_IMPROVING = Wand
    ITEMS_PRICES: dict = {
        WandOfFire: 100,
        WandOfWater: 100,
        WandOfEarth: 100,
        WandOfLightning: 100,
        WandOfShadow: 100,
    }


class AmateurEnchanter(Enchanter):
    MARGIN: float = 0.5


class ExperiencedEnchanter(Enchanter):
    MARGIN: float = 0.6
