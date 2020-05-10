from enums import PlayerClasses
from eq.defense import MagicResistance, Defense
from items.defensive_items.abstract_defensive_items import Gloves


class RustyGloves(Gloves):
    NAME: str = "Zardzewiałe rękawice"
    RESISTANCE: MagicResistance = MagicResistance(fire=1, water=1, earth=1, lightning=1, shadow=1)
    WEARABLE_FOR: tuple = (
        PlayerClasses.MAGE,
        PlayerClasses.KNIGHT,
        PlayerClasses.PALADIN,
    )
    STARTING_DEFENSE = Defense(2)


class PlateGloves(Gloves):
    NAME: str = "Rękawice płytowe"
    RESISTANCE: MagicResistance = MagicResistance(fire=2, water=2, earth=2, lightning=2, shadow=2)
    WEARABLE_FOR: tuple = (
        PlayerClasses.KNIGHT,
        PlayerClasses.PALADIN
    )
    STARTING_DEFENSE = Defense(5)


class MysticalGloves(Gloves):
    NAME: str = "Mityczne rękawice"
    RESISTANCE: MagicResistance = MagicResistance(fire=5, water=5, earth=5, lightning=10, shadow=10)
    WEARABLE_FOR: tuple = (
        PlayerClasses.MAGE,
    )
    STARTING_DEFENSE = Defense(5)
