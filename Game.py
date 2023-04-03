"""
"""
from Resources import Resources
from Routes import Routes
from Map import Map
from Player import Player


class Game:
    def __init__(self):
        self.map = Map()
        self.resources = Resources()
        self.routes = Routes()
        self.player_1 = Player()
        self.player_2 = Player()

    def start_game(self):