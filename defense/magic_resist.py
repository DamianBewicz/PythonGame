class MagicResist:

    def __init__(self) -> None:
        self.resistance = {
            "fire": 0,
            "water": 0,
            "earth": 0,
            "lightning": 0,
            "shadow": 0
        }

    def __str__(self) -> str:
        return ""

    def raise_resist(self, type: str, value: int) -> None:
        self.resistance[type] += value

    def get_resistance_value(self, type: str) -> int:
        return self.resistance[type]


a = MagicResist()
print(a.raise_resist("water", 15))
print(a.raise_resist("water", 10))
print(a.resistance["water"])
