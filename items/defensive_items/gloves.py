from defense.magic_resist import MagicResistance
from enums import PlayerClasses
from items.defensive_items.abstract_defensive_items import Gloves


class RustyGloves(Gloves):
    NAME: str = "Zardzewiałe rękawice"
    RESISTANCE: MagicResistance = MagicResistance(fire=1, water=1, earth=1, lightning=1, shadow=1)
    WEARABLE_FOR: tuple = (
        PlayerClasses.MAGE,
        PlayerClasses.KNIGHT,
        PlayerClasses.PALADIN,
    )

    def __init__(self) -> None:
        super().__init__()
        self.defense: int = 2


class MysticalGloves(Gloves):
    NAME: str = "Mityczne rękawice"
    RESISTANCE: MagicResistance = MagicResistance(fire=5, water=5, earth=5, lightning=10, shadow=10)
    WEARABLE_FOR: tuple = (
        PlayerClasses.MAGE,
    )

    def __init__(self) -> None:
        super().__init__()
        self.defense: int = 5
