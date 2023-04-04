"""
"""
from random import shuffle


class Resources:
    def __init__(self):
        self.main = 0
        self.color_count = [14, 12, 12, 12, 12, 12, 12, 12, 12] # Index cooresponds with unique color, value is count
        self.deck = []
        self.discard = []
        self.visible = []
        # create deck
        self.create_deck()
        self.shuffle()
        # deal 4 cards to each player (DO THIS IN GAME.py)
        # add top five cards to visible (DO THIS IN GAME.py)

    def create_deck(self):
        self.deck = []
        for color in range(len(self.color_count)):
            self.deck.extend([color for i in range(self.color_count[color])])

    def shuffle(self):
        self.deck.extend(self.discard)
        self.discard = []
        shuffle(self.deck)

    def draw_top(self):
        if len(self.deck) <= 0:
            self.shuffle()
        return self.deck.pop(0)

    def draw_visible(self, n):
        card = self.visible[n]
        self.visible[n] = self.draw_top()
        self.three_wilds()
        return card

    def three_wilds(self):
        # if three wilds in visible
        wild_count = 0
        for i in self.visible:
            if i == 0:
                wild_count += 1
        if wild_count >= 3:
            self.discard.extend(self.visible)
            self.discard = []
            self.place_visible()

    def place_visible(self):
        for i in range(5):
            self.visible.append(self.draw_top())

    def return_cards(self, cards):
        self.discard.extend(cards)