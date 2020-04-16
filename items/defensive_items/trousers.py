from defense.magic_resist import MagicResistance
from enums import PlayerClasses
from items.defensive_items.abstract_defensive_items import Trousers


class RustyTrousers(Trousers):
    NAME: str = "Zardzewiałe spodnie"
    RESISTANCE: MagicResistance = MagicResistance(fire=1, water=1, earth=1, lightning=1, shadow=1)
    WEARABLE_FOR: tuple = (
        PlayerClasses.KNIGHT,
        PlayerClasses.PALADIN,
        PlayerClasses.MAGE,
    )

    def __init__(self) -> None:
        super().__init__()
        self.defense: int = 3


class PhoenixTrousers(Trousers):
    NAME: str = "Gacie Feniksa"
    RESISTANCE: MagicResistance = MagicResistance(fire=15, water=0, earth=10, lightning=5, shadow=5)
    WEARABLE_FOR: tuple = (
        PlayerClasses.MAGE,
    )

    def __init__(self) -> None:
        super().__init__()
        self.defense: int = 10


