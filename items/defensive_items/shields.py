from items.defensive_items.abstract_items import Shield


class RustedShield(Shield):
    NAME = "Zardzewiała tarcza"

    def __init__(self):
        super().__init__()
        self.defense = 15
        self.percent_block_chance = 15
