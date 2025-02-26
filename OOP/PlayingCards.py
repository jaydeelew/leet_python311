from enum import Enum, auto
from typing import Any


class Card:
    @property
    def card_value(self) -> int:
        raise NotImplementedError()

    def __lt__(self, other):
        return self.card_value < other.card_value


# We use auto here since the order and values don't matter.
# The values are only This is needed to distinguish the suits.
class Suit(Enum):
    CLUBS = auto()  # 1
    DIAMONDS = auto()  # 2
    HEARTS = auto()  # 3
    SPADES = auto()  # 4
    JOKER = auto()  # 5


# The values here do matter since they are chosen to correspond to the card values.
class CardValue(Enum):
    ACE = 1
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


class PlayingCard(Card):
    # Maps suit names (str) to Suit enum values
    # Example: "Clubs" -> Suit.CLUBS (value: 1)
    # This is needed to find self.__value in __init__
    SUIT_VALUE = {
        "Clubs": Suit.CLUBS,
        "Diamonds": Suit.DIAMONDS,
        "Hearts": Suit.HEARTS,
        "Spades": Suit.SPADES,
    }

    # Maps enum values (Suit) to suit names (str)
    # Example: Suit.CLUBS -> "Clubs"
    # This is needed to find suit in __str__
    VALUE_SUIT = {e: n for n, e in SUIT_VALUE.items()}

    # Maps card values (str) to CardValue enum values
    # Example: "A" -> CardValue.ACE
    # This is needed to find self.__value in __init__
    CODE_CARDVALUE = {
        "A": CardValue.ACE,
        # This is a dictionary comprehension that creates mappings from string numbers ("2" through "10")
        # to their corresponding CardValue enum members. For example, "2" -> CardValue.TWO
        **{str(i): getattr(CardValue, CardValue(i).name) for i in range(2, 11)},
        "J": CardValue.JACK,
        "Q": CardValue.QUEEN,
        "K": CardValue.KING,
    }

    # Maps CardValue enum values to card values (str)
    # Example: CardValue.ACE -> "A"
    # This is needed to find value in __str__
    CARDVALUE_CODE = {e: n for n, e in CODE_CARDVALUE.items()}

    def __init__(self, suit: str, value: str):
        super().__init__()  # Not necessary since super class has no __init__.
        self.__suit: Suit = self.SUIT_VALUE[suit]
        self.__value: CardValue = self.CODE_CARDVALUE[value]

    @property
    def card_value(self) -> int:
        return self.__value.value

    def __str__(self) -> str:
        value = self.CARDVALUE_CODE[self.__value]
        suit = self.VALUE_SUIT[self.__suit]
        return f"{value} of {suit}"


class JokerColor(Enum):
    RED = auto()
    BLACK = auto()


class Joker(Card):
    # Maps color names (str) to JokerColor enum values
    # Example: "Red" -> JokerColor.RED
    # This is needed to find self.__color in __init__
    COLORS_TO_ENUMS = {
        "Red": JokerColor.RED,
        "Black": JokerColor.BLACK,
    }
    # Maps enum values (JokerColor) to color names (str)
    # Example: JokerColor.RED -> "Red"
    # This is needed to return the color in __str__
    ENUMS_TO_COLORS = {e: n for n, e in COLORS_TO_ENUMS.items()}

    def __init__(self, color: str):
        super().__init__()  # Not necessary since super class has no __init__.
        self.__color: JokerColor = self.COLORS_TO_ENUMS[color]

    @property
    def card_value(self):
        return 14

    def __str__(self) -> str:
        return f"{self.ENUMS_TO_COLORS[self.__color]} Joker"


class Hand:
    @property
    def hand_value(self) -> int:
        raise NotImplementedError()

    def __lt__(self, other):
        return self.hand_value < other.hand_value


class GameHand(Hand):
    def __init__(self) -> None:
        self.__cards: list[Card] = []

    def add_card(self, new_card: Card) -> None:
        self.__cards.append(new_card)

    @property
    def get_hand(self):
        return self.__cards

    def __lt__(self, other: "GameHand | Any") -> bool:
        a_cards_objs = self.__cards
        b_cards_objs = other.get_hand
        a_values = [card.card_value for card in a_cards_objs]
        b_values = [card.card_value for card in b_cards_objs]
        a_values.sort(reverse=True)
        b_values.sort(reverse=True)

        i = j = 0
        while i < len(a_values) and j < len(b_values):
            if a_values[i] == b_values[j]:
                i += 1
                j += 1
                continue
            if a_values[i] > b_values[j]:
                return True
            else:
                return False

        return False


class Game:
    def __init__(self) -> None:
        self.__cards: list[Card] = []
        self.__hands: list[GameHand] = []

    def add_card(self, suit: str, value: str) -> None:
        self.__cards.append(PlayingCard(suit, value))

    def card_string(self, card: int) -> str:
        return str(self.__cards[card])

    def last_card_string(self) -> str:
        return str(self.__cards[-1])

    def card_beats(self, card_a: int, card_b: int) -> bool:
        return self.__cards[card_a] > self.__cards[card_b]

    def list_cards(self) -> None:
        for number, card in enumerate(self.__cards):
            print(f"{number}: {self.card_string(number)}")

    def add_joker(self, color: str) -> None:
        self.__cards.append(Joker(color))

    def add_hand(self, card_indices: list[int]) -> None:
        new_hand = GameHand()
        for card_id in card_indices:
            new_hand.add_card(self.__cards[card_id])
        self.__hands.append(new_hand)

    def hand_string(self, hand: int) -> str:
        # For each card object in the hand, convert it to a string and join them with a comma.
        return ", ".join(str(card) for card in self.__hands[hand].get_hand)

    def beats_hand(self, hand_a: int, hand_b: int) -> bool:
        return hand_a > hand_b


if __name__ == "__main__":
    game = Game()

    for _ in range(4):
        suit, value = input("Enter the suit and card value seperated by a space: ").split()
        game.add_joker(value) if suit == "Joker" else game.add_card(suit, value)
        print(game.last_card_string())

    game.list_cards()

    game.add_hand([0, 2])
    game.add_hand([1, 3])

    if game.beats_hand(0, 1):
        print(f"Hand 0: {game.hand_string(0)} beats Hand 1: {game.hand_string(1)}")
    else:
        print(f"Hand 1: {game.hand_string(1)} beats Hand 0: {game.hand_string(0)}")
