from random import shuffle
from characters.player.player import Player


class Deck:
    def __init__(self) -> None:
        self.cards: list = [
            Card(suit, rank, value)
            for suit in Card.SUITS
            for rank, value in Card.RANKS.items()
        ]

    def shuffle(self) -> None:
        shuffle(self.cards)


class PlayerHand:
    def __init__(self) -> None:
        self.cards: list = []
        self.stand: bool = False

    def __str__(self) -> str:
        hand = ''
        for card in self.cards:
            hand += f'{card}\n'
        return "Karty gracza:\n" + hand

    @property
    def points(self) -> int:
        points = 0
        for card in self.cards:
            points += card.value
        return points

    def has_blackjack(self) -> bool:
        return self.points == 21

    def make_decision(self, dealer) -> None:
        while True:
            answer = input("Czy chcesz dobrać kartę?\n"
                           "Tak\n"
                           "Nie\n")
            if answer.capitalize() == "Tak":
                return dealer.give_card(self)
            elif answer.capitalize() == "Nie":
                self.stand = True
                break
            print("\nPodana wartość jest nieprawidłowa!\n")

    @staticmethod
    def wants_another_game() -> bool:
        choices = {
            "tak": True,
            "nie": False
        }
        while True:
            try:
                choice = input("\nCzy chcesz zagrać jeszcze jedną gre?\n"
                               "Tak\n"
                               "Nie\n")
                return choices[choice.lower()]
            except KeyError:
                print("\nPodana wartość jest nieprawidłowa\n")


class Dealer:
    def __init__(self, deck) -> None:
        self.deck: Deck = deck
        self.cards: list = []
        self.bet: int = 0
        self.min_bet: int = 10
        self.max_bet: int = 200
        self.has_finished: bool = False

    def __str__(self) -> str:
        hand = ''
        for card in self.cards:
            hand += f'{card}\n'
        return "Karty krupiera:\n" + hand

    def have_money_for_game(self, player: Player) -> bool:
        return player.equipment.gold.amount > self.min_bet

    def shuffle_deck(self) -> None:
        shuffle(self.deck.cards)

    def take_bet(self, player: Player) -> None:
        while True:
            try:
                bet = int(input("Ile pieniędzy chcesz przeznaczyć na grę.\n"
                                "Minimalna wartość zakładu: {}\n"
                                "Maksymalna wartość zakładu: {}\n".format(self.min_bet, self.max_bet)))
                if self.min_bet <= bet <= self.max_bet:
                    player.equipment.gold.subtract(bet)
                    self.bet += bet
                    break
                print("\nPodana wartość jest wartość jest spoza przedziału, spróbuj jeszcze raz.\n")
            except (ValueError, KeyError, AttributeError):
                print("Podana wartość jest nieprawidłowa, spróbuj jeszcze raz!\n")

    def give_card(self, player_hand: PlayerHand) -> None:
        player_hand.cards.append(self.deck.cards.pop())

    def take_card(self) -> None:
        self.cards.append(self.deck.cards.pop())

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
                winning_money = self.bet * 3
                player.equipment.gold.add(winning_money)
            elif self.points > player_hand.points:
                print("Przegrałeś!\n")
            elif self.points == player_hand.points:
                print("Remis!")
                player.equipment.gold.add(self.bet)
            self.has_finished = True
            break

    @property
    def points(self) -> int:
        points = 0
        for card in self.cards:
            points += card.value
        return points


class Card:
    SUITS = (
        "Serce",
        "Dzwonek",
        "Żołądź",
        "Wino",
    )
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


class Blackjack:
    def __init__(self) -> None:
        self.player_hand = PlayerHand()
        self.dealer = Dealer(Deck())
        self.wants_to_play = True

    def play_game(self, player) -> None:
        self.dealer.deck.shuffle()
        print()
        self.dealer.take_bet(player)
        self.dealer.deal_starting_cards(self.player_hand)
        while True:
            print()
            print(self.player_hand)
            self.dealer.show_card()
            self.player_hand.make_decision(self.dealer)
            if self.player_hand.points > 21 or self.player_hand.stand:
                print(self.player_hand)
                self.dealer.end_game(self.player_hand, player)
            if self.dealer.has_finished:
                break

    @staticmethod
    def main(player) -> None:
        while True:
            print()
            print(player.equipment.gold)
            b = Blackjack()
            if b.dealer.have_money_for_game(player):
                b.play_game(player)
                if b.player_hand.wants_another_game():
                    continue
                else:
                    break
            else:
                print("\nNie masz pieniędzy na gre\n")
                break
