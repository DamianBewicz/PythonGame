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
        resist_string = "Twoje odporności\n"
        for index, (resistance, value) in enumerate(self.resistance.items()):
            resist_string += "{:20}: {}\n".format(colored(resistance.value.capitalize(), colors[index]), str(value))
        return resist_string

    def raise_resist(self, magic_type: MagicNature, value: int) -> None:
        self.resistance[magic_type] += value

    def get_resistance_value(self, magic_type: MagicNature) -> int:
        return self.resistance[magic_type]


a = MagicResistance()
print(a)
