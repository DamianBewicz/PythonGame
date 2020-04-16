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

    def __init__(self) -> None:
        super().__init__()
        self.defense: int = 2


class ArchmageHeadpiece(Helmet):
    NAME: str = "Hełm arcymaga"
    RESISTANCE: MagicResistance = MagicResistance(fire=5, water=5, earth=5, lightning=5, shadow=5)
    WEARABLE_FOR: tuple = (
        PlayerClasses.MAGE,
    )

    def __init__(self) -> None:
        super().__init__()
        self.defense: int = 5



