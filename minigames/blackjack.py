from random import shuffle


class Player:
    def __init__(self) -> None:
        self.gold = 100
        self.hand = []


class Dealer:
    def __init__(self, deck) -> None:
        self.deck = deck
        self.rejected_card = []
        self.hand = []
        self.bet = 0
        self.min_bet = 10
        self.max_bet = 50

    def shuffle_deck(self) -> None:
        shuffle(self.deck)

    def take_bet(self, player) -> None:
        while True:
            try:
                bet = int(input("Ile pieniędzy chcesz przeznaczyć na grę.\n"
                                "minimalna wartość zakładu: {}\n"
                                "maksymalna wartość zakładu: {}\n".format(self.min_bet, self.max_bet)))
                if self.min_bet <= bet <= self.max_bet:
                    player.gold -= bet
                    self.bet += bet
                    break
                print("Podana wartość jest wartość jest spoza przedziału, spróbuj jeszcze raz.\n")
            except (ValueError, KeyError, AttributeError):
                print("Podana wartość jest nieprawidłowa, spróbuj jeszcze raz!\n")

    def have_money_for_game(self, player):
        return player.money < self.min_bet

    def deal_cards(self, player):
        pass


class Deck:
    def __init__(self, cards) -> None:
        self.cards = cards


class Card:
    SUITS = ["Heart", "Tile", "Clover", "Pike"]
    RANKS = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10,
        "A": 11,
    }

    def __init__(self, suit, rank, value) -> None:
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return "{} {}".format(self.rank, self.suit)


def main():
    deck = [Card(suit, rank, value)
            for suit in Card.SUITS
            for rank, value in Card.RANKS.items()]
    dealer = Dealer(deck)
    player = Player()
    dealer.shuffle_deck()

    dealer.take_bet(player)


if __name__ == "__main__":
    main()
