"""
"""
from random import shuffle


class Resources:
    def __init__(self):
        self.main = 0
        self.color_count = [14, 12, 12, 12, 12, 12, 12, 12, 12]  # Index corresponds with unique color, value is count
        self.deck = []
        self.discard = []
        self.face_up = []
        # create deck
        self.create_deck()
        self.shuffle()

    def create_deck(self):
        self.deck = []
        for color in range(len(self.color_count)):
            self.deck.extend([color for _ in range(self.color_count[color])])

    def shuffle(self):
        self.deck.extend(self.discard)
        self.discard = []
        shuffle(self.deck)

    def draw_top(self):
        remaining_cards = len(self.deck) + len(self.discard)
        if remaining_cards == 0:
            return None
        if len(self.deck) <= 0:
            self.shuffle()
        return self.deck.pop(0)

    def draw_face_up(self, n):
        card = self.face_up[n]
        self.face_up[n] = self.draw_top()
        self.check_three_wilds()
        return card

    def check_three_wilds(self):
        # if three wilds in visible
        wild_count = 0
        for card in self.face_up:
            if card == 0:
                wild_count += 1
        if wild_count >= 3:
            self.place_face_up()

    def place_face_up(self):
        self.discard.extend(self.face_up)
        self.face_up = [self.draw_top() for card in range(5)]
        self.check_three_wilds()

    def return_cards(self, cards):
        self.discard.extend(cards)
