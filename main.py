from Routes import Routes, Ticket
from Resources import Resources
from Map import Map
from Game import Game
from Player import Player
from Bots.RandomAI import RandomAI
from Bots.TrentonAI import TrentonAI
from Bots.BelnapAI import BelnapAI
from Bots.RolloAI import RolloAI
import networkx as nx
from math import log
import matplotlib.pyplot as plt
from test import get_map
import os
from test import get_map, get_tickets, plot_histogram, plot_score_difference


def main(n):
    scores = []
    for i in range(n):
        G = get_map("defaultMap.txt")
        tickets = get_tickets('defaultTickets.txt')
        routes = Routes(tickets)
        resources = Resources()
        players = [RandomAI(), RolloAI(), TrentonAI(), BelnapAI()]
        # Next step, pass all into Game
        game = Game(G, routes, resources, players)
        if n < 10:
            game.map.display_map()
            game.plot_scores("Scores")
        scores.append(game.scores[-1])
    if n >= 10:
        plot_histogram(scores)
        plot_score_difference(scores)


main(1)
