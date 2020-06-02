from enums import PlayerClasses
from eq.defense import MagicResistance, Defense
from items.defensive_items.abstract_defensive_items import Shield


class RustyShield(Shield):
    NAME = "Zardzewiała tarcza"
    BLOCK_CHANCE = 50
    RESISTANCE: MagicResistance = MagicResistance(fire=1, water=1, earth=1, lightning=1, shadow=1)
    WEARABLE_FOR: tuple = (
        PlayerClasses.KNIGHT,
        PlayerClasses.PALADIN,
    )
    STARTING_DEFENSE: Defense = Defense(2)


class BurnishedShield(Shield):
    NAME = "Wypolerowana tarcza"
    BLOCK_CHANCE = 20
    RESISTANCE: MagicResistance = MagicResistance(fire=2, water=2, earth=2, lightning=2, shadow=2)
    WEARABLE_FOR: tuple = (
        PlayerClasses.KNIGHT,
        PlayerClasses.PALADIN,
    )
    STARTING_DEFENSE: Defense = Defense(10)


class IronShield(Shield):
    NAME = "Żelazna tarcza"
    BLOCK_CHANCE = 30
    RESISTANCE: MagicResistance = MagicResistance(fire=3, water=3, earth=3, lightning=3, shadow=3)
    WEARABLE_FOR: tuple = (
        PlayerClasses.KNIGHT,
        PlayerClasses.PALADIN,
    )
    STARTING_DEFENSE: Defense = Defense(15)
