"""
"""
from random import randint


class Player:
    def __init__(self):
        self.player_id = None
        self.resources = []
        self.routes = []
        self.temp_routes = []
        self.points = 0
        self.trains = 45
        self.G = None
        self.desired_railroads = []
        self.desired_resources = []
        self.node_map = {}
        self.edge_map = {}

    def create_map(self, G):
        self.G = G

        i = 0
        for node in self.G.nodes():
            self.node_map[node] = i
            i += 1

        i = 0
        for edge in self.G.edges(keys=True):
            self.edge_map[i] = edge
            self.G[edge[0]][edge[1]][edge[2]]['edge_id'] = i
            i += 1

    def set_player_id(self, player_id):
        self.player_id = player_id

    def remove_claimed_edges(self, claimed_edges):
        # claimed edges must be of form G.edges(data='claimed_by, keys=True)
        for u, v, k, c in claimed_edges:
            if self.G.has_edge(u, v, k) and c != self.player_id:
                self.G.remove_edge(u, v, key=k)

    def take_turn(self):
        return (0, 0)
    
    def choose_resources(self, i):
        choices = [i for i in range(6)]
        
        return randint(0, 6)

    def evaluate_routes(self):
        # determine which routes to keep
        
        return 0

    def evaluate_roads(self):
        return 0

    def evaluate_cards(self):
        return 0
        
    def get_resource(self, resource):
        self.resources.append(resource)
        
    def get_route(self, route):
        self.temp_routes.append(route)

    def buy_railroad(self, edge):
        # edge = (u, v, k, {'data': value})

        for i in range(edge['cost']):
            print("buy")
            # get from self.resources
            # same color first (what if it has no color?)
            # then wild
        return 0
        


