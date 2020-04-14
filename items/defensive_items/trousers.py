from items.defensive_items.abstract_items import Trousers


class RustedTrousers(Trousers):
    NAME = "Zardzewiałe spodnie"

    def __init__(self) -> None:
        super().__init__()
        self.defense = 10
