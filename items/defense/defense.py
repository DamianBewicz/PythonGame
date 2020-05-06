class Defense:
    def __init__(self, armor=0) -> None:
        self.ammount = armor

    def __str__(self) -> str:
        return f"{self.ammount} punktów pancerza"

    def __add__(self, other):
        return Defense(self.ammount + other.ammount)

    def __sub__(self, other):
        return Defense(self.ammount - other.ammount)
