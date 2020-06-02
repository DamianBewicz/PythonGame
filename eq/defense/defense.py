class Defense:
    def __init__(self, armor=0) -> None:
        self.amount = armor

    def __str__(self) -> str:
        return f"{self.amount} punktów pancerza"

    def __add__(self, other):
        return Defense(self.amount + other.amount)

    def __sub__(self, other):
        return Defense(self.amount - other.amount)
