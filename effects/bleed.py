from effects.effect import Effect


class Bleed(Effect):
    def __init__(self, chance) -> None:
        super().__init__()
        self.type = "Dynamic"
        self.duration = 3
        self.effect_chance = chance
        self.damage = 5

    def __str__(self):
        return "Krwawisz!"

    def perform_action(self, character) -> None:
        print(self)
        character.hp -= self.damage
