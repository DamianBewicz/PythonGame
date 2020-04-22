from defense.magic_resist import MagicResistance
from enums import PlayerClasses
from items.defensive_items.abstract_defensive_items import Helmet


class RustyHelmet(Helmet):
    NAME: str = "Zardzewiały hełm"
    RESISTANCE: MagicResistance = MagicResistance(fire=1, water=1, earth=1, lightning=1, shadow=1)
    WEARABLE_FOR: tuple = (
        PlayerClasses.KNIGHT,
        PlayerClasses.PALADIN,
        PlayerClasses.MAGE,
    )
    STARTING_DEFENSE = 2


class PlateHelmet(Helmet):
    NAME: str = "Hełm płytowy"
    RESISTANCE: MagicResistance = MagicResistance(fire=2, water=2, earth=2, lightning=2, shadow=2)
    WEARABLE_FOR: tuple = (
        PlayerClasses.KNIGHT,
        PlayerClasses.PALADIN
    )
    STARTING_DEFENSE = 10


class ArchmageHeadpiece(Helmet):
    NAME: str = "Hełm arcymaga"
    RESISTANCE: MagicResistance = MagicResistance(fire=5, water=5, earth=5, lightning=5, shadow=5)
    WEARABLE_FOR: tuple = (
        PlayerClasses.MAGE,
    )
    STARTING_DEFENSE = 5
