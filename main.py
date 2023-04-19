from Routes import Routes, Destination
from Resources import Resources
from Map import Map
from Game import Game
from Player import Player
from RandomAI import RandomAI
from TrentonAI import TrentonAI
import networkx as nx
from math import log
import matplotlib.pyplot as plt
from test import get_map, get_routes
import os


def main(n):
    for trial in range(n):
        G = get_map("defaultMap.txt")
        destinations = get_routes('defaultRoutes.txt')
        routes = Routes(destinations)
        resources = Resources()
        players = [RandomAI(), RandomAI(), TrentonAI()]
        # Next step, pass all into Game
        game = Game(G, routes, resources, players)
        game.map.display_map()


main(1)
