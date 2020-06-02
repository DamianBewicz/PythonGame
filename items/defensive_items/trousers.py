from enums import PlayerClasses
from eq.defense import MagicResistance, Defense
from items.defensive_items.abstract_defensive_items import Trousers


class RustyTrousers(Trousers):
    NAME: str = "Zardzewiałe spodnie"
    RESISTANCE: MagicResistance = MagicResistance(fire=1, water=1, earth=1, lightning=1, shadow=1)
    WEARABLE_FOR: tuple = (
        PlayerClasses.KNIGHT,
        PlayerClasses.PALADIN,
        PlayerClasses.MAGE,
    )
    STARTING_DEFENSE: Defense = Defense(3)


class PlateTrousers(Trousers):
    NAME: str = "Spodnie płytowe"
    RESISTANCE: MagicResistance = MagicResistance(fire=2, water=2, earth=2, lightning=2, shadow=2)
    WEARABLE_FOR: tuple = (
        PlayerClasses.KNIGHT,
        PlayerClasses.PALADIN
    )
    STARTING_DEFENSE: Defense = Defense(15)


class PhoenixTrousers(Trousers):
    NAME: str = "Spodnie Feniksa"
    RESISTANCE: MagicResistance = MagicResistance(fire=15, water=0, earth=10, lightning=5, shadow=5)
    WEARABLE_FOR: tuple = (
        PlayerClasses.MAGE,
    )
    STARTING_DEFENSE: Defense = Defense(5)
