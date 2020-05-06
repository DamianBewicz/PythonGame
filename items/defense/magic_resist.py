from enums import MagicNature
from termcolor import colored


class MagicResistance:

    def __init__(self, fire: int = 0, water: int = 0, earth: int = 0, lightning: int = 0, shadow: int = 0) -> None:
        self.resistance = {
            MagicNature.FIRE: fire,
            MagicNature.WATER: water,
            MagicNature.EARTH: earth,
            MagicNature.LIGHTNING: lightning,
            MagicNature.SHADOW: shadow,
        }

    def __str__(self) -> str:
        colors = ["red", "blue", "yellow", "grey", "white"]
        resist_string = "\nTwoje odporności\n"
        for index, (resistance, value) in enumerate(self.resistance.items()):
            resist_string += "{:20}: {}\n".format(colored(resistance.value.capitalize(), colors[index]), str(value))
        return resist_string

    def __add__(self, other):
        return MagicResistance(
            self.resistance[MagicNature.FIRE] + other.resistance[MagicNature.FIRE],
            self.resistance[MagicNature.WATER] + other.resistance[MagicNature.WATER],
            self.resistance[MagicNature.EARTH] + other.resistance[MagicNature.EARTH],
            self.resistance[MagicNature.LIGHTNING] + other.resistance[MagicNature.LIGHTNING],
            self.resistance[MagicNature.SHADOW] + other.resistance[MagicNature.SHADOW]
        )

    def __sub__(self, other):
        return MagicResistance(
            self.resistance[MagicNature.FIRE] - other.resistance[MagicNature.FIRE],
            self.resistance[MagicNature.WATER] - other.resistance[MagicNature.WATER],
            self.resistance[MagicNature.EARTH] - other.resistance[MagicNature.EARTH],
            self.resistance[MagicNature.LIGHTNING] - other.resistance[MagicNature.LIGHTNING],
            self.resistance[MagicNature.SHADOW] - other.resistance[MagicNature.SHADOW]
        )

    def get_value(self, magic_type: MagicNature) -> int:
        return self.resistance[magic_type]


magic_resistance1 = MagicResistance(fire=5, water=5, earth=5, lightning=5, shadow=5)
magic_resistance2 = MagicResistance(fire=5, water=10, earth=5, lightning=5, shadow=5)
print(magic_resistance1 + magic_resistance2)

