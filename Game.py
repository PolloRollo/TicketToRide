"""


"""
from Resources import Resources
from Routes import Routes
from Map import Map
from Player import Player
from RandomAI import RandomAI
import copy
from random import shuffle


class Game:
    def __init__(self, G, routes, resources):
        # parameters: Map, Resources, Routes, Player_list
        self.resources = resources
        self.routes = routes
        self.players = [RandomAI() for i in range(2)]
        self.map = Map(G, len(self.players))
        self.actions = 2
        self.end = 30

        # Begin game, take turns, test
        self.start_game()
        self.take_turns()
        self.test()

    def start_game(self):
        """
        Shuffle resource and route decks. Deal each player 4 resources and 3 routes.
        Ask each player which routes they will keep. Player must keep at least 2.
        Place 5 resource cards face up. Give each player a deepcopy of the map.
        """
        self.resources.shuffle()
        self.routes.shuffle()

        # shuffle(self.players)

        self.deal_resources()
        self.deal_routes(start=True)
        self.resources.place_visible()
        self.give_map_copy(self.map.G)
        # print(self.map.all_edges())

    def set_player_id(self):
        for i in range(len(self.players)):
            self.players.set_player_id(i)

    def deal_resources(self):
        for deal in range(4):  # Perhaps add a parameter where this could be changed, self.initial_hand
            for player in self.players:
                player.get_resource(self.resources.draw_top())

    def deal_routes(self, start=False):
        for player in self.players:
            self.draw_routes(player, start)

    def give_map_copy(self, G):
        for player in self.players:
            player.create_map(copy.deepcopy(G))

    def end_conditions(self):
        trains = [player.trains for player in self.players]
        for i in trains:
            if i <= 2 and self.end > len(self.players):
                self.end = len(self.players)
        if self.end > 0:
            self.end -= 1
            return False
        return True

    def take_turns(self):
        turn = 0
        while not self.end_conditions():
            player = self.players[turn % len(self.players)]
            self.actions = 2
            claimed_edges = self.map.G.edges(data='claimed_by', keys=True)
            player.remove_claimed_edges(claimed_edges)

            while self.actions > 0:
                action, details = player.take_turn(self.actions, self.resources.visible)
                if action == 0: # draw cards
                    self.draw_cards(player, details)
                elif action == 1: # build train
                    return 0
                elif action == 2: # take routes
                    self.draw_routes(player)
            turn += 1
        return 0

    def draw_cards(self, player, choice):
        if choice < 5:
            if self.resources.visible[choice] == 0:
                self.actions -= 1
            player.get_resource(self.resources.draw_visible(choice))
        else:
            player.get_resource(self.resources.draw_top())
        self.actions -= 1
        """
        # Need to then specify what will be drawn.
        for i in range(2):
            choice = p.choose_resources(i)
            if choice < 5:
                wild = False
                if self.resources.visible[choice] == 0:
                    wild = True
                p.get_resource(self.resources.draw_visible(choice))
                if wild:
                    return 0
            else:
                p.get_resource(self.resources.draw_top())
        """

    def draw_routes(self, player, start=False):
        for deal in range(3):  # Similar, self.number_of_new_routes
            player.get_route(self.routes.draw_top())
        if start:
            player.choose_routes(min=2)
            # decide on resources, maybe make two methods.
        else:
            player.choose_routes()
        self.actions -= 2

    def test(self):
        print(self.resources.visible)

        for player in self.players:
            print(player.resources)
            for route in player.routes:
                print(route.get_destinations(), route.get_points())

    def print_log(self):
        return 0

