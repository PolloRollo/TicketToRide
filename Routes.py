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
        if len(self.deck) <= 0:
            self.shuffle()
        return self.deck.pop(0)

    def return_cards(self, cards):
        self.discard.extend(cards)


class Destination:
    def __init__(self, A, B, points):
        self.A = A
        self.B = B
        self.points = points

    def get_points(self):
        return self.points

    def get_destinations(self):
        return (self.A, self.B)