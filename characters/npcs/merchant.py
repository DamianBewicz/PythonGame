class Merchant:
    def __init__(self) -> None:
        self.items = []
        self.margin = 0.75
        self.merchant_actions = [
            ("Sprzedaj", self.buy_item),
            ("Kup", self.sell_item),
            ("Wróć", "cos"),
        ]

    def choose_action(self, player) -> None:
        print("\nWybierz akcje\n")
        for number, action in enumerate(self.merchant_actions):
            print(number + 1, action[0])
        choice = int(input())
        self.merchant_actions[choice - 1][1](player)

    def sell_item(self, player) -> bool:
        print("\nWybierz przedmiot który chcesz kupić\n")
        for number, item in enumerate(self.items):
            print(number + 1, item)
        choice = int(input())
        if player.money >= self.items[choice - 1].cost and not player.backpack.is_full():
            player.backpack.add(self.items[choice - 1])
            return True
        print("\nNie można dokonąć zakupu!\n")
        return False

    def buy_item(self, player) -> bool:
        if not player.backpack.is_empty():
            print("\nWybierz przedmiot na sprzedaż\n")
            for number, item in enumerate(player.backpack.items):
                print(number + 1, item)
            choice = int(input())
            removed_item = player.backpack.items.pop(choice - 1)
            player.money += removed_item.cost * self.margin
            return True
        print("\nNie masz przedmiotów na sprzedaż!\n")
        return False
