from random import shuffle


class Player:
    def __init__(self) -> None:
        self.gold = 100


class PlayerHand:
    def __init__(self) -> None:
        self.cards = []
        self.stand = False

    def __str__(self) -> str:
        hand = ''
        for card in self.cards:
            hand += f'{card}\n'
        return "Karty gracza:\n" + hand

    def make_decision(self, dealer) -> None:
        while True:
            try:
                answer = input("Czy chcesz dobrać kartę?\n"
                               "Tak\n"
                               "Nie\n")
                if answer.capitalize() == "Tak":
                    return dealer.give_card(self)
                elif answer.capitalize() == "Nie":
                    self.stand = True
                    break
                print("Podana wartość jest nieprawidłowa!")
            except AttributeError:
                print("Podana wartość jest nieprawidłowa!")

    @property
    def points(self) -> int:
        points = 0
        for card in self.cards:
            points += card.value
        return points


class Dealer:
    def __init__(self, deck) -> None:
        self.deck = deck
        self.rejected_card = []
        self.cards = []
        self.bet = 0
        self.min_bet = 10
        self.max_bet = 50
        self.has_finished = False

    def __str__(self) -> str:
        hand = ''
        for card in self.cards:
            hand += f'{card}\n'
        return "Karty krupiera:\n" + hand

    def have_money_for_game(self, player: Player) -> bool:
        return player.gold < self.min_bet

    def shuffle_deck(self) -> None:
        shuffle(self.deck)

    def take_bet(self, player: Player) -> None:
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

    def give_card(self, player_hand: PlayerHand) -> None:
        player_hand.cards.append(self.deck.pop())

    def take_card(self) -> None:
        self.cards.append(self.deck.pop())

    def deal_starting_cards(self, player_hand: PlayerHand) -> None:
        for starting_cards in range(2):
            self.give_card(player_hand)
            self.take_card()

    def show_card(self) -> None:
        print("Karty krupiera:\n"
              "{}\n".format(self.cards[0]))

    def end_game(self, player_hand: PlayerHand, player: Player) -> None:
        while True:
            print(self)
            if self.points < player_hand.points <= 21:
                print("Dobieram karte!\n")
                self.take_card()
                continue
            elif player_hand.points > 21:
                print("Przekroczyłeś 21 punktów!\n"
                      "Przegrałeś!\n")
            elif self.points > 21:
                print("Wygrałeś!\n")
                player.gold += round(self.bet * 2.5)
            elif self.points > player_hand.points:
                print("Przegrałeś!\n")
            elif self.points == player_hand.points:
                print("Remis!")
                player.gold += self.bet
            self.has_finished = True
            break

    @property
    def points(self) -> int:
        points = 0
        for card in self.cards:
            points += card.value
        return points


class Card:
    SUITS = ["Serce", "Dzwonek", "Żołądź", "Wino"]
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

    def __str__(self) -> str:
        return "{} {}".format(self.rank, self.suit)


def main():
    deck = [Card(suit, rank, value)
            for suit in Card.SUITS
            for rank, value in Card.RANKS.items()]
    player = Player()
    player_hand = PlayerHand()
    dealer = Dealer(deck)
    dealer.shuffle_deck()
    dealer.take_bet(player)
    dealer.deal_starting_cards(player_hand)
    while True:
        print(player_hand)
        dealer.show_card()
        player_hand.make_decision(dealer)
        if player_hand.points > 21 or player_hand.stand:
            print(player_hand)
            dealer.end_game(player_hand, player)
        if dealer.has_finished:
            break


if __name__ == "__main__":
    main()
