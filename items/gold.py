class Gold:
    def __init__(self) -> None:
        self.ammount: int = 10000

    def __str__(self):
        return "Masz {} złota".format(str(self.ammount))

    def add(self, ammount: int) -> None:
        self.ammount += ammount

    def subtract(self, ammount: int) -> None:
        self.ammount -= ammount
