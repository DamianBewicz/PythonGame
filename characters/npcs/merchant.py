class Merchant:
    def __init__(self) -> None:
        self.items = []
        self.margin = 0.75
        self.merchant_actions = [
            ("Sprzedaj", self.sell_item),
            ("Kup", self.buy_item),
        ]

    def choose_action(self, player) -> None:
        while True:
            print("\nWybierz akcje, jeśli chcesz wyjść naciśnij enter\n")
            for number, action in enumerate(self.merchant_actions):
                print(number + 1, action[0])
            choice = input()
            if choice == "":
                break
            self.merchant_actions[int(choice) - 1][1](player)

    def buy_item(self, player) -> bool:
        while True:
            print(f"\nWybierz przedmiot który chcesz kupić, kliknij enter żeby wyjść\nPieniądze gracza - {player.money}\n"
                  f"Dostępne miejsce - {player.backpack.avaible_slots}\n")
            for number, item in enumerate(self.items):
                print(number + 1, item, f"\nCena przedmiotu - {item.cost}\n")
            choice = input()
            if choice == "":
                return False
            elif player.money >= self.items[int(choice) - 1].cost and not player.backpack.is_full():
                player.backpack.add(self.items[int(choice) - 1])
                player.money -= self.items[int(choice) - 1].cost
                return True
            print("\nNie można dokonąć zakupu!\n")
            return False

    def sell_item(self, player) -> bool:
        while True:
            if not player.backpack.is_empty():
                print(f"\nWybierz przedmiot na sprzedaż, jeśli chcesz wyjść naciśnij enter."
                      f"\nPieniądze gracza - {player.money}\n")
                for number, item in enumerate(player.backpack.items):
                    print(number + 1, item, f"\nKoszt kupna przedmiotu - {round(item.cost*self.margin)}\n")
                choice = input()
                if choice == "":
                    return False
                removed_item = player.backpack.items.pop(int(choice) - 1)
                player.money += round(removed_item.cost * self.margin)
                player.backpack.avaible_slots += 1
                return True
            print("\nNie masz przedmiotów na sprzedaż!\n")
            return False
