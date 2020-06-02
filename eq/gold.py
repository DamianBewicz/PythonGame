class Gold:
    def __init__(self) -> None:
        self.amount: int = 10000

    def __str__(self):
        return "Masz {} złota".format(str(self.amount))

    def add(self, amount: int) -> None:
        self.amount += amount

    def subtract(self, amount: int) -> None:
        self.amount -= amount
