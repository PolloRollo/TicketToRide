"""
The Routes class holds all the Desitination cards.

"""
from random import shuffle


class Routes:
    def __init__(self, cards):
        self.deck = cards
        self.discard = []

    def shuffle(self):
        self.deck.extend(self.discard)
        self.discard = []
        shuffle(self.deck)

    def draw(self):
        remaining_cards = len(self.deck) + len(self.discard)
        if remaining_cards >= 3:
            return [self.draw_top() for _ in range(3)]
        else:
            return [self.draw_top() for _ in range(remaining_cards)]


    def draw_top(self):
        if len(self.deck) <= 0:
            self.shuffle()
        return self.deck.pop(0)

    def return_cards(self, cards):
        self.discard.extend(cards)


class Destination:
    def __init__(self, A, B, points):
        self.__A = A
        self.__B = B
        self.__points = points

    def get_points(self):
        return self.__points

    def get_destinations(self):
        return (self.__A, self.__B)