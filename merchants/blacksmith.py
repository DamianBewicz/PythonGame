from items import Scythe, Cudgel, Axe, RustySword, BattleAxe, Inquisitor, MasterSword
from items.weapons.abstract_weapons import MeleeWeapon
from merchants.merchant import WeaponImprover


class Blacksmith(WeaponImprover):
    IMPROVE_PRICE: int = 30
    WEAPON_FOR_IMPROVING = MeleeWeapon


class AmateurBlacksmith(Blacksmith):
    ITEMS_PRICES: dict = {
        Scythe: 50,
        Cudgel: 55,
        Axe: 60,
        RustySword: 80,
    }
    MARGIN: float = 0.5


class ExperiencedBlacksmith(Blacksmith):
    ITEMS_PRICES: dict = {
        BattleAxe: 150,
        Inquisitor: 250,
        MasterSword: 400,
    }
    MARGIN: float = 0.6
