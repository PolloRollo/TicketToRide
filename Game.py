"""


"""
import networkx as nx
import matplotlib.pyplot as plt
from Resources import Resources
from Routes import Routes
from Map import Map
from Player import Player
from RandomAI import RandomAI
import copy
from random import shuffle


class Game:
    def __init__(self, G, routes, resources, players):
        # parameters: Map, Resources, Routes, Player_list
        self.resources = resources
        self.routes = routes
        self.players = players
        self.map = Map(G, len(self.players))

        # Game Constants
        self.actions = 2
        self.railroad_points = {0: 0, 1: 1, 2: 2, 3: 4, 4: 7, 5: 10, 6: 15}
        self.end = 1000

        self.scores = []

        # Begin game, take turns, test
        self.start_game()
        self.take_turns()

    def start_game(self):
        """
        Shuffle resource and route decks. Deal each player 4 resources and 3 routes.
        Ask each player which routes they will keep. Player must keep at least 2.
        Place 5 resource cards face up. Give each player a deepcopy of the map.
        """
        self.resources.shuffle()
        self.routes.shuffle()
        self.set_player_id()

        # shuffle(self.players)

        self.deal_resources()
        self.deal_routes()
        self.resources.place_face_up()
        self.give_map_copy(self.map.G)

    def set_player_id(self):
        for i in range(len(self.players)):
            self.players[i].set_player_id(i)

    def deal_resources(self):
        for deal in range(4):  # Perhaps add a parameter where this could be changed, self.initial_hand
            for player in self.players:
                player.get_resource(self.resources.draw_top())

    def deal_routes(self):
        for player in self.players:
            self.draw_routes(player, start=True)

    def give_map_copy(self, G):
        for player in self.players:
            player.create_map(copy.deepcopy(G))

    def end_conditions(self):
        trains = [player.trains for player in self.players]
        for i in trains:
            if i <= 2 and self.end > len(self.players):
                self.end = len(self.players)
        if self.end == 0:
            return True
        if len(self.resources.deck) + len(self.resources.discard) <= 10:
            return True
        if len(self.routes.deck) + len(self.routes.discard) <= 3:
            return True
        self.end -= 1
        return False

    def take_turns(self):
        turn = 0
        while not self.end_conditions():
            player = self.players[turn % len(self.players)]
            self.actions = 2
            # Update player's map
            claimed_edges = self.map.G.edges(data='claimed_by', keys=True)
            player.remove_claimed_edges(claimed_edges)

            while self.actions > 0:
                option, details = player.take_turn(self.actions, self.resources.face_up)
                if option == 0:  # draw cards
                    self.draw_cards(player, details)
                elif option == 1:  # build train
                    self.build_railroad(player, details)
                elif option == 2:  # take routes
                    self.draw_routes(player)
            turn += 1
            self.scores.append(self.score_game())
        print(self.scores[-1])
        # print(turn)
        return 0

    def draw_cards(self, player, choice):
        if choice < 5:
            if self.resources.face_up[choice] == 0:
                self.actions -= 1  # Extra point deducted for taking wild
            player.get_resource(self.resources.draw_face_up(choice))
        else:
            player.get_resource(self.resources.draw_top())
        self.actions -= 1

    def build_railroad(self, player, data):
        edge, desired_color = data

        u, v, k = edge
        cost = self.map.G[u][v][k]['cost']

        discard = player.buy_railroad(edge, desired_color, cost)
        self.resources.discard.extend(discard)
        self.map.claim_edge(player, edge)
        self.actions -= 2

    def draw_routes(self, player, start=False):
        for route in self.routes.draw():  # Similar, self.number_of_new_routes
            player.get_route(route)
        discard = None
        if start:
            discard = player.choose_routes(min=2)
        else:
            discard = player.choose_routes()
        self.routes.return_cards(discard)
        self.actions -= 2

    def score_game(self):
        score = [self.score_player(player) for player in self.players]
        # Longest train (lol this might be difficult)

        return score

    def score_player(self, player):
        score = 0

        # Points per railroad built
        for edge in self.map.get_edges(data='claimed_by', keys=True):
            u, v, k, claim = edge
            if claim is not None and claim == player.player_id:
                cost = self.map.G[u][v][k]['cost']
                score += self.railroad_points[cost]

        # Points per route completed
        for route in player.routes:
            A, B = route.get_destinations()
            if player.node_map[A] == player.node_map[B]:
                score += route.get_points()
            else:
                score -= route.get_points()

        return score

    def plot_scores(self, title):
        score_by_player = [[] for p in self.players]
        for time in range(len(self.scores)):
            for player in self.players:
                score_by_player[player.player_id].append(self.scores[time][player.player_id])
        plt.title(title)
        for player in self.players:
            plt.plot(score_by_player[player.player_id], label=str(type(player)) + str(player.player_id))
        plt.xlabel("Turn")
        plt.ylabel("Score")
        plt.legend()
        plt.show()
