import networkx as nx
# from math import log
import matplotlib.pyplot as plt
import os
from Resources import Resources
from Routes import Routes, Ticket
# from Map import Map
from Game import Game
from Player import Player
from RandomAI import RandomAI
from RolloAI import RolloAI
from BelnapAI import BelnapAI


def test(n, plots=False):
    scores = []
    for i in range(n):
        G = get_map("defaultMap.txt")
        tickets = get_tickets('defaultTickets.txt')
        routes = Routes(tickets)
        resources = Resources()
        players = [RolloAI(), RolloAI()]
        # Next step, pass all into Game
        game = Game(G, routes, resources, players)
        if plots:
            game.map.display_map()
            game.plot_scores("Scores")
            # for player in game.players:
                # print(player.resources)
        scores.append(game.scores[-1])
    if n >= 10:
        plot_histogram(scores)
        plot_score_difference(scores)


def LFRBenchmark(n, tau1=2.5, tau2=1.5, average_degree=7.0, mu=.1, min_degree=None, max_degree=None, min_community=30, max_community=70):
    """ !!! only min_degree XOR average_degree must be specified, otherwise a NetworkXError is raised. !!!
    Benchmark test to determine how well an algorithm is at community detection.
    Returns networkx graph object
    """
    if min_degree is not None:
        average_degree = None
    if max_degree is None:
        max_degree = n
    # Initialize graph
    G = None
    try:
        G = nx.generators.community.LFR_benchmark_graph(n=n, tau1=tau1, tau2=tau2, average_degree=average_degree, mu=mu,
                                                        min_degree=min_degree, max_degree=max_degree, min_community=min_community, max_community=max_community)
    except nx.ExceededMaxIterations:
        return G
    G.remove_edges_from(nx.selfloop_edges(G))
    return G


def get_map(file):
    edge_data = [('color', int), ('cost', int)]
    G = nx.read_edgelist(file, delimiter=', ', data=edge_data, create_using=nx.MultiGraph)
    return G


def get_tickets(file):
    if not os.access(file, 0):
        print("Error: Failed to access file")
    f = open(file, 'r')
    tickets = []
    for line in f:
        A, B, points = line.split(', ')
        points = int(points)
        tickets.append(Ticket(A, B, points))
    return tickets


def plot_histogram(scores):
    # This is a good way to compare the performance of different agents
    plt.title("Scores")
    for player in range(len(scores[0])):
        player_score = [scores[i][player] for i in range(len(scores))]
        plt.hist(player_score, bins=20, histtype='step')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()


def plot_score_difference(scores):
    # Designed for two player games, will only compare player 0 and 1
    score_dif = []
    for time in scores:
        score_dif.append(time[1] - time[0])
    plt.title("Score difference: Player 1 - Player 0")
    plt.hist(score_dif, bins=20, histtype='step')
    plt.xlabel("Turn")
    plt.ylabel("Score")
    plt.show()


color_dict = {"Colors.none": 0,
              "Colors.red": 1,
              "Colors.orange": 2,
              "Colors.yellow": 3,
              "Colors.green": 4,
              "Colors.blue": 5,
              "Colors.pink": 6,
              "Colors.white": 7,
              "Colors.black": 8}


# test(2, True)
# test(200, False)
