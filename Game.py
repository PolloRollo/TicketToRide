"""
"""
from Resources import Resources
from Routes import Routes
from Map import Map
from Player import Player


class Game:
    def __init__(self):
        # parameters: Map, Resources, Routes, Player_list
        self.map = Map()
        self.resources = Resources()
        self.routes = Routes()
        self.player_1 = Player()
        self.player_2 = Player()

    def start_game(self):


    def take_turns(self):

    def end_conditions(self):

