from Routes import Routes, Ticket
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
from test import get_map, get_tickets


def main(n):
    for trial in range(n):
        G = get_map("defaultMap.txt")
        tickets = get_tickets('defaultTickets.txt')
        routes = Routes(tickets)
        resources = Resources()
        players = [RandomAI(), RandomAI(), TrentonAI()]
        # Next step, pass all into Game
        game = Game(G, routes, resources, players)
        game.map.display_map()
        game.plot_scores("Scores")


main(1)
