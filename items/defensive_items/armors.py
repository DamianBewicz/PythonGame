from defense.magic_resist import MagicResistance
from enums import PlayerClasses
from items.defensive_items.abstract_defensive_items import Armor


class RustyArmor(Armor):
    NAME: str = "Zardzewiała zbroja"
    RESISTANCE: MagicResistance = MagicResistance(fire=1, water=1, earth=1, lightning=1, shadow=1)
    WEARABLE_FOR: tuple = (
        PlayerClasses.MAGE,
        PlayerClasses.KNIGHT,
        PlayerClasses.PALADIN
    )

    def __init__(self) -> None:
        super().__init__()
        self.defense: int = 5


class PlateArmor(Armor):
    NAME: str = "Zbroja płytowa"
    RESISTANCE: MagicResistance = MagicResistance(fire=3, water=3, earth=3, lightning=3, shadow=3)
    WEARABLE_FOR: tuple = (
        PlayerClasses.MAGE,
    )

    def __init__(self) -> None:
        super().__init__()
        self.defense: int = 20


class ArchmageRobe(Armor):
    NAME: str = "Szata arcymaga"
    RESISTANCE: MagicResistance = MagicResistance(fire=10, water=10, earth=10, lightning=10, shadow=10)
    WEARABLE_FOR: tuple = (
        PlayerClasses.MAGE,
    )

    def __init__(self) -> None:
        super().__init__()
        self.defense: int = 10



