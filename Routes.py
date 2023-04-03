"""
"""
from random import shuffle


class Routes:
    def __init__(self):
        self.main = 0
        self.deck = []
        self.discard = []

    def shuffle(self):
        self.deck.extend(self.discard)
        self.discard = []
        shuffle(self.deck)

    def draw(self):
        return [self.draw_top() for _ in range(3)]

    def draw_top(self):
        # if deck > 0, otherwise shuffle discard
        return self.deck.pop(0)

    def return_cards(self, cards):
        self.discard.extend(cards)