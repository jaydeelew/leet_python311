"""
TODO:
- Limit number of players
- Add a draw option
- Test PlayingCard.__lt__()
"""

from enum import Enum, auto
from typing import Any
import random
from collections import Counter


# The values here do matter since they are chosen to correspond to the card values.
class CardValue(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14


# We use auto here since the order and values don't matter.
# The values are only needed to distinguish the suits.
class Suit(Enum):
    CLUBS = auto()  # 1
    DIAMONDS = auto()  # 2
    HEARTS = auto()  # 3
    SPADES = auto()  # 4


SUIT_TO_ENUM = {
    "Clubs": Suit.CLUBS,
    "Diamonds": Suit.DIAMONDS,
    "Hearts": Suit.HEARTS,
    "Spades": Suit.SPADES,
}

ENUM_TO_SUIT = {v: s for s, v in SUIT_TO_ENUM.items()}

CARD_TO_ENUM = {
    "Two": CardValue.TWO,
    "Three": CardValue.THREE,
    "Four": CardValue.FOUR,
    "Five": CardValue.FIVE,
    "Six": CardValue.SIX,
    "Seven": CardValue.SEVEN,
    "Eight": CardValue.EIGHT,
    "Nine": CardValue.NINE,
    "Ten": CardValue.TEN,
    "Jack": CardValue.JACK,
    "Queen": CardValue.QUEEN,
    "King": CardValue.KING,
    "Ace": CardValue.ACE,
}

ENUM_TO_CARD = {v: s for s, v in CARD_TO_ENUM.items()}


class Card:
    @property
    def get_value(self) -> int:
        raise NotImplementedError()

    def __lt__(self, other: "Card") -> bool:
        return self.get_value < other.get_value


class PlayingCard(Card):
    def __init__(self, cardValue: CardValue, suitValue: Suit):
        self._card_value = cardValue
        self._suit_value = suitValue

    @property
    def get_value(self) -> CardValue:
        return self._card_value

    @property
    def get_suit(self) -> Suit:
        return self._suit_value

    def __lt__(self, other: "Card") -> bool:
        return self.get_value.value < other.get_value.value

    def __str__(self) -> str:
        value = ENUM_TO_CARD[self.get_value]
        suit = ENUM_TO_SUIT[self.get_suit]
        return f"{value} of {suit}"


class Hand:
    def __init__(self, cards: list[Card]) -> None:
        self._cards = cards
        self._hand_value = None

    @property
    def get_hand(self) -> list:
        raise NotImplementedError()

    @property
    def hand_value(self):
        raise NotImplementedError()

    def __lt__(self, other):
        raise NotImplementedError()


class PokerHand(Hand):
    class PokerHands(Enum):
        ROYAL_FLUSH = 10
        STRAIGHT_FLUSH = 9
        FOUR_OF_A_KIND = 8
        FULL_HOUSE = 7
        FLUSH = 6
        STRAIGHT = 5
        THREE_OF_A_KIND = 4
        TWO_PAIR = 3
        ONE_PAIR = 2
        HIGH_CARD = 1

    def __init__(self, cards: list[Card]) -> None:
        super().__init__(cards)
        self._hand_value = self.best_hand()

    @property
    def get_hand(self) -> list:
        cards = []
        cards.append(self._hand_value[0].name)
        for card in self._cards:
            cards.append(str(card))
        return cards

    @property
    def hand_value(self):
        return self._hand_value

    def add_card(self, card: Card) -> None:
        self._cards.append((card))

    def remove_card(self, card_value: CardValue, suit: Suit) -> bool:
        for card in self._cards:
            if card.get_value == card_value and card.get_suit == suit:
                self._cards.remove(card)
                return True
        return False

    # This works by comparing the tuple returned by this Pokerhand's _hand_value to another Pokerhand.
    def __lt__(self, other: "PokerHand | Any") -> bool:
        # Determine if the two hands are equal in order of hands.
        # We need to append .value to self.hand_value[0] since this is an Enum.
        if self._hand_value[0].value == other._hand_value[0].value:
            match self._hand_value[0].value:
                case self.PokerHands.ROYAL_FLUSH.value:
                    return False
                case self.PokerHands.STRAIGHT_FLUSH.value:
                    return self._hand_value[1] < other._hand_value[1]
                case self.PokerHands.FOUR_OF_A_KIND.value:
                    return self._hand_value[1] < other._hand_value[1]
                case self.PokerHands.FULL_HOUSE.value:
                    if self._hand_value[1] < other._hand_value[1]:
                        return True
                    elif self._hand_value[1] > other._hand_value[1]:
                        return False
                    # If the three of a kinds are equal, compare the pairs.
                    elif self._hand_value[2] < other._hand_value[2]:
                        return True
                    # If the other pair is <= to this pair return False
                    return False
                case self.PokerHands.FLUSH.value:
                    for i in range(1, 6):
                        if self._hand_value[i] < other._hand_value[i]:
                            return True
                        elif self._hand_value[i] > other._hand_value[i]:
                            return False
                    # If all the card values are equal:
                    return False
                case self.PokerHands.STRAIGHT.value:
                    return self._hand_value[1] < other._hand_value[1]
                case self.PokerHands.THREE_OF_A_KIND.value:
                    if self._hand_value[1] < other._hand_value[1]:
                        return True
                    elif self._hand_value[1] > other._hand_value[1]:
                        return False
                    else:
                        for i in range(2, 4):
                            if self._hand_value[i] < other._hand_value[i]:
                                return True
                            elif self._hand_value[i] > other._hand_value[i]:
                                return False
                        # If the remaining card values are equal:
                        return False
                case self.PokerHands.TWO_PAIR.value:
                    if self._hand_value[1] < other._hand_value[1]:
                        return True
                    elif self._hand_value[1] > other._hand_value[1]:
                        return False
                    # If the higher value pairs are equal, compare the lower value pairs.
                    elif self._hand_value[2] < other._hand_value[2]:
                        return True
                    elif self._hand_value[2] > other._hand_value[2]:
                        return False
                    # If both pairs are equal in value, look to the remaining card.
                    elif self._hand_value[3] < other._hand_value[3]:
                        return True
                    # If the remaining card values are equal:
                    return False
                case self.PokerHands.ONE_PAIR.value:
                    if self._hand_value[1] < other._hand_value[1]:
                        return True
                    elif self._hand_value[1] > other._hand_value[1]:
                        return False
                    # Since the pairs are equal:
                    else:
                        for i in range(2, 5):
                            if self._hand_value[i] < other._hand_value[i]:
                                return True
                            elif self._hand_value[i] > other._hand_value[i]:
                                return False
                        # If the remaining card values are equal:
                        return False
                case self.PokerHands.HIGH_CARD.value:
                    return self._hand_value[1] < other._hand_value[1]
        else:
            return self._hand_value[0].value < other._hand_value[0].value

    # Best hand returns a tuple of the highest value of the hand.
    def best_hand(self) -> tuple[PokerHands, int, int, int, int, int]:
        def check_high_card():
            return max(values)

        def check_one_pair() -> bool:
            pair_count = 0
            for val in values_to_counts.values():
                if val == 2:
                    pair_count += 1
            return pair_count == 1

        def check_two_pair() -> bool:
            pair_count = 0
            for val in values_to_counts.values():
                if val == 2:
                    pair_count += 1
            return pair_count == 2

        def check_three_kind() -> bool:
            for val in values_to_counts.values():
                if val == 3:
                    return True
            return False

        def check_straight() -> bool:
            for i in range(1, len(values)):
                if values[i] - values[i - 1] != 1:
                    return False
            return True

        def check_flush() -> bool:
            return len(suits) == 1

        def check_full_house() -> bool:
            return one_pair and three_kind

        def check_four_kind() -> bool:
            for val in values_to_counts.values():
                if val == 4:
                    return True
            return False

        def check_straight_flush() -> bool:
            return flush and straight

        def check_royal_flush() -> bool:
            return straight_flush and high_card == "Ace"

        # A -1 in indexes 1-5 of the return tuple indicates value not used.
        # Royal Flush does not need any index 1-5.
        # Four of a Kind places its value at index 1, and the fifth card at index 2.
        # Straigt Flush, Straight, and High Card place High Card at index 1.
        # Full House places its Three of a Kind value at index 1, and the pair value at index 2.
        # Flush places all five card values in descending order in indexes 1-5.
        # Three of a Kind places its value at index 1, and the remaining card values in descending at index 2 and 3.
        # Two Pair places its higher value at index 1, and second value at index 2.
        # Pair places its value at index 1, and the other three value in descending order at indexes 2-4.
        # and the remaining card in the third int value.
        def result_tuple(hand: self.PokerHands) -> tuple[self.PokerHands, int, int, int, int, int]:
            match hand:
                case self.PokerHands.ROYAL_FLUSH:
                    return (hand, -1, -1, -1, -1, -1)
                case self.PokerHands.STRAIGHT_FLUSH:
                    return (hand, high_card, -1, -1, -1, -1)
                case self.PokerHands.FOUR_OF_A_KIND:
                    for val, cnt in values_to_counts.items():
                        if cnt == 4:
                            fok = val
                        if cnt == 1:
                            fifth = val
                    return (hand, fok, fifth, -1, -1, -1)
                case self.PokerHands.FULL_HOUSE:
                    pair = 0
                    three = 0
                    for val, cnt in values_to_counts.items():
                        if cnt == 2:
                            pair = val
                        if cnt == 3:
                            three = val
                    return (hand, three, pair, -1, -1, -1)
                case self.PokerHands.FLUSH:
                    a = values_to_counts[4]
                    b = values_to_counts[3]
                    c = values_to_counts[2]
                    d = values_to_counts[1]
                    e = values_to_counts[0]
                    return (hand, a, b, c, d, e)
                case self.PokerHands.STRAIGHT:
                    return (hand, high_card, -1, -1, -1, -1)
                case self.PokerHands.THREE_OF_A_KIND:
                    other_cards = []
                    for val, cnt in values_to_counts.items():
                        if cnt == 3:
                            tok = val
                        if cnt == 1:
                            other_cards.append(val)
                    higher = max(other_cards)
                    lower = min(other_cards)
                    return (hand, tok, higher, lower, -1, -1)
                case self.PokerHands.TWO_PAIR:
                    pairs = []
                    for val, cnt in values_to_counts.items():
                        if cnt == 2:
                            pairs.append(val)
                        if cnt == 1:
                            remaining = val
                    higher = max(pairs)
                    lower = min(pairs)
                    return (hand, higher, lower, remaining, -1, -1)
                case self.PokerHands.ONE_PAIR:
                    other_cards = []
                    for val, cnt in values_to_counts.items():
                        if cnt == 2:
                            pair = val
                        if cnt == 1:
                            other_cards.append(val)
                    other_cards.sort(reverse=True)
                    b = other_cards[0]
                    c = other_cards[1]
                    d = other_cards[2]
                    return (hand, pair, b, c, d, -1)
                case self.PokerHands.HIGH_CARD:
                    other_cards = []
                    for val in values_to_counts.keys():
                        other_cards.append(val)
                    other_cards.sort(reverse=True)
                    a = other_cards[0]
                    b = other_cards[1]
                    c = other_cards[2]
                    d = other_cards[3]
                    e = other_cards[4]
                    return (hand, a, b, c, d, e)

        suits = {card.get_suit.name for card in self._cards}
        values = [card.get_value.value for card in self._cards]
        values.sort()
        values_to_counts = Counter(values)

        high_card = check_high_card()  # High card holds actual card value.
        one_pair = check_one_pair()
        two_pair = check_two_pair()
        three_kind = check_three_kind()
        flush = check_flush()
        straight = check_straight()
        full_house = check_full_house()
        four_kind = check_four_kind()
        straight_flush = check_straight_flush()
        royal_flush = check_royal_flush()

        hands = [
            (royal_flush, self.PokerHands.ROYAL_FLUSH),
            (straight_flush, self.PokerHands.STRAIGHT_FLUSH),
            (four_kind, self.PokerHands.FOUR_OF_A_KIND),
            (full_house, self.PokerHands.FULL_HOUSE),
            (flush, self.PokerHands.FLUSH),
            (straight, self.PokerHands.STRAIGHT),
            (three_kind, self.PokerHands.THREE_OF_A_KIND),
            (two_pair, self.PokerHands.TWO_PAIR),
            (one_pair, self.PokerHands.ONE_PAIR),
            (True, self.PokerHands.HIGH_CARD),  # Always true as fallback
        ]

        for is_hand, hand_type in hands:
            if is_hand:  # True if these cards make up this hand.
                return result_tuple(hand_type)


class Deck:
    def __init__(self) -> None:
        self._deck: dict[int, Card] = {}
        self._dealt: list[int] = []
        self._build_deck()

    def _build_deck(self) -> None:
        count = 1
        for suit in Suit:
            for value in CardValue:
                new_card = PlayingCard(value, suit)
                self._deck[count] = new_card
                count += 1

    def random_deal(self, hand_size: int) -> list[Card]:
        hand = []
        # Convert range to set and remove dealt cards via set subtraction.
        available_cards = set(range(1, len(self._deck) + 1)) - set(self._dealt)
        # Convert back to list for random.sample.
        sample = random.sample(list(available_cards), hand_size)

        for card_num in sample:
            hand.append(self._deck[card_num])
            self._dealt.append(card_num)

        return hand

    def random_deal_one(self) -> PlayingCard:
        # Convert range to set and remove dealt cards via set subtraction.
        available_cards = set(range(1, len(self._deck) + 1)) - set(self._dealt)
        # Convert back to list for random.sample.
        sample = random.sample(list(available_cards), 1)
        return self._deck[sample[0]]

    def reset_deck(self) -> None:
        self._dealt.clear()

    def print_deck(self) -> None:
        for i, card in self._deck.items():
            print(i, str(card))


class Player:
    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def get_name(self) -> str:
        return self._name


class PokerGame:
    def __init__(self) -> None:
        self._draw = False
        self._num_players = 0
        while True:
            ans = input("Would you like to play 5 card draw? y/n: ")
            if ans in {"y", "Y", "n", "N"}:
                ans = ans.lower()
                if ans == "y":
                    self._draw = True
                break
            else:
                print("You must enter y or n")
                input("Press Enter to continue...")

        while True:
            ans = input("Enter the number of players: ")
            try:
                self._num_players = int(ans)
            except ValueError:
                print("Invalid input. Please enter a number")
                input("Press Enter to continue...")
                continue

            if self._draw and self._num_players > 6:
                print("There must be 2 to 6 players in a game of 5 card draw\n")
                continue
            elif self._num_players > 10:
                print("There must be 2 to 10 players in a game of 5 card stud\n")
                continue

            break

        self._deck: Deck = Deck()
        self._players: dict[Player, PokerHand | None] = {}
        self.add_players(self._num_players)

    @property
    def draw_game(self):
        return self._draw

    def add_players(self, num_players: int) -> None:
        for _ in range(num_players):
            name = input("Enter a player's name: ")
            self._players[Player(name)] = None

    def deal_cards(self, hand_size: int) -> None:
        for player in self._players:
            hand = self._deck.random_deal(hand_size)
            self._players[player] = PokerHand(hand)

    def show_hand(self, player: Player) -> None:
        hand = self._players[player]
        if hand:  # Check if hand exists
            print(f"\n{player.get_name}'s ", end="")
            match hand.hand_value[0].value:
                case PokerHand.PokerHands.ROYAL_FLUSH.value:
                    sorted_cards = sorted(hand._cards, key=lambda x: x.get_value.value)
                    print("Royal Flush:", ", ".join(str(card) for card in sorted_cards))

                case PokerHand.PokerHands.STRAIGHT_FLUSH.value:
                    sorted_cards = sorted(hand._cards, key=lambda x: x.get_value.value)
                    print("Straight Flush:", ", ".join(str(card) for card in sorted_cards))

                case PokerHand.PokerHands.FOUR_OF_A_KIND.value:
                    # Group four matching cards first, then the remaining card
                    four_value = hand.hand_value[1]
                    four_cards = [card for card in hand._cards if card.get_value.value == four_value]
                    other_card = [card for card in hand._cards if card.get_value.value != four_value]
                    print("Four of a Kind:", ", ".join(str(card) for card in four_cards + other_card))

                case PokerHand.PokerHands.FULL_HOUSE.value:
                    # Group three matching cards first, then the pair
                    three_value = hand.hand_value[1]
                    pair_value = hand.hand_value[2]
                    three_cards = [card for card in hand._cards if card.get_value.value == three_value]
                    pair_cards = [card for card in hand._cards if card.get_value.value == pair_value]
                    print("Full House:", ", ".join(str(card) for card in three_cards + pair_cards))

                case PokerHand.PokerHands.FLUSH.value:
                    # Sort by value since they're all the same suit
                    sorted_cards = sorted(hand._cards, key=lambda x: x.get_value.value, reverse=True)
                    print("Flush:", ", ".join(str(card) for card in sorted_cards))

                case PokerHand.PokerHands.STRAIGHT.value:
                    sorted_cards = sorted(hand._cards, key=lambda x: x.get_value.value)
                    print("Straight:", ", ".join(str(card) for card in sorted_cards))

                case PokerHand.PokerHands.THREE_OF_A_KIND.value:
                    three_value = hand.hand_value[1]
                    three_cards = [card for card in hand._cards if card.get_value.value == three_value]
                    other_cards = sorted(
                        [card for card in hand._cards if card.get_value.value != three_value],
                        key=lambda x: x.get_value.value,
                        reverse=True,
                    )
                    print("Three of a Kind:", ", ".join(str(card) for card in three_cards + other_cards))

                case PokerHand.PokerHands.TWO_PAIR.value:
                    high_pair = hand.hand_value[1]
                    low_pair = hand.hand_value[2]
                    high_pair_cards = [card for card in hand._cards if card.get_value.value == high_pair]
                    low_pair_cards = [card for card in hand._cards if card.get_value.value == low_pair]
                    other_card = [card for card in hand._cards if card.get_value.value not in (high_pair, low_pair)]
                    print("Two Pair:", ", ".join(str(card) for card in high_pair_cards + low_pair_cards + other_card))

                case PokerHand.PokerHands.ONE_PAIR.value:
                    pair_value = hand.hand_value[1]
                    pair_cards = [card for card in hand._cards if card.get_value.value == pair_value]
                    other_cards = sorted(
                        [card for card in hand._cards if card.get_value.value != pair_value],
                        key=lambda x: x.get_value.value,
                        reverse=True,
                    )
                    print("One Pair:", ", ".join(str(card) for card in pair_cards + other_cards))

                case PokerHand.PokerHands.HIGH_CARD.value:
                    sorted_cards = sorted(hand._cards, key=lambda x: x.get_value.value, reverse=True)
                    print("High Card:", ", ".join(str(card) for card in sorted_cards))

    def show_all_hands(self) -> None:
        for player in self._players.keys():
            self.show_hand(player)

    def draw_cards(self) -> None:
        for player in self._players:
            num_cards_trading = 0
            while True:
                ans = input(f"\n{player.get_name}, how many cards are you trading in (0-3)? ")
                try:
                    num_cards_trading = int(ans)
                except ValueError:
                    print("Invalid input. Please enter a number")
                    input("Press Enter to continue ...")
                    continue

                if not 0 <= num_cards_trading <= 3:
                    print("You must enter a number from 0 to 3")
                    input("Press Enter to continue ...")
                else:
                    break

            curr_num_cards = 0
            while curr_num_cards < num_cards_trading:
                trade = input("Enter the card you are trading (e.g. Two of Hearts): ").split()
                # Is trade is a valid card?
                if trade[0] in CARD_TO_ENUM and trade[2] in SUIT_TO_ENUM:
                    # If the player is holding this card, remove the card from the players hand.
                    if self._players[player].remove_card(CARD_TO_ENUM[trade[0]], SUIT_TO_ENUM[trade[2]]):
                        new_card = self._deck.random_deal_one()
                        self._players[player].add_card(new_card)
                        curr_num_cards += 1
                    else:
                        print(f"{player.get_name} does not have a {trade[0]} of {trade[2]} to trade in")
                        input("Press Enter to continue ...")
                else:
                    print("Invalid card. Please enter a valid card value and suit.")
                    input("Press Enter to continue ...")

    def winner(self) -> Player:
        winner = None
        winning_hand = None

        for player, hand in self._players.items():
            if winner is None:
                winner = player
                winning_hand = hand
            elif hand > winning_hand:
                winner = player
                winning_hand = hand

        return winner


if __name__ == "__main__":
    game = PokerGame()
    game.deal_cards(5)
    game.show_all_hands()
    if game.draw_game:
        game.draw_cards()
    game.show_all_hands()
    winning_player = game.winner()
    print("\nAnd the winner is ... ", end="")
    game.show_hand(winning_player)
