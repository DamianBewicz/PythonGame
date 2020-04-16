from defense.magic_resist import MagicResistance
from enums import PlayerClasses
from items.defensive_items.abstract_defensive_items import Shield


class RustyShield(Shield):
    NAME = "Zardzewiała tarcza"
    BLOCK_CHANCE = 15
    RESISTANCE: MagicResistance = MagicResistance(fire=1, water=1, earth=1, lightning=1, shadow=1)
    WEARABLE_FOR: tuple = (
        PlayerClasses.KNIGHT,
        PlayerClasses.PALADIN,
    )

    def __init__(self) -> None:
        super().__init__()
        self.defense: int = 2
