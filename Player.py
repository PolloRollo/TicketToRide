"""
"""
from random import randint
import networkx as nx


class Player:
    def __init__(self):
        self.player_id = None
        self.resources = []
        self.routes = []
        self.temp_routes = []
        self.points = 0  # Do we need this in player? Probably
        self.trains = 45
        self.G = None

        self.desired_railroads = []
        self.desired_resources = []

        self.node_map = {}
        self.edge_map = {}
        self.resource_count = {}

    def create_map(self, G):
        self.G = G
        i = 0
        for edge in self.G.edges(keys=True):
            self.edge_map[i] = edge
            self.G[edge[0]][edge[1]][edge[2]]['edge_id'] = i
            i += 1
        i = 0
        for node in self.G.nodes():
            self.node_map[node] = i
            i += 1
        nx.relabel_nodes(self.G, self.node_map, copy=False)

    def set_player_id(self, player_id):
        self.player_id = player_id

    def remove_claimed_edges(self, claimed_edges):
        # claimed edges must be of form G.edges(data='claimed_by, keys=True)
        for u, v, k, c in claimed_edges:
            if self.G.has_edge(u, v, k) and c != self.player_id:
                self.G.remove_edge(u, v, key=k)
        
    def get_resource(self, resource):
        self.resources.append(resource)
        
    def get_route(self, route):
        self.temp_routes.append(route)

    def check_can_buy(self, edge, desired_color):
        u, v, k, data = edge
        A = self.node_map(u)
        B = self.node_map(v)
        self.count_resources()
        if data['color'] == 0: # Railroad can be paid by any color
            if self.count_resources[desired_color] >= data['cost']:
                return True, (data['cost'], 0)
            elif self.count_resources[desired_color] + self.count_resources[0] >= data['cost']:
                count = self.count_resources[desired_color]
                return True, (count, data['cost'] - count)
        elif data['color'] == desired_color: # Railroad can only be paid by same color
            if self.count_resources[data['color']] >= data['cost']:
                return True, (data['cost'], 0)
            elif self.count_resources[data['color']] + self.count_resources[0] >= data['cost']:
                count = self.count_resources[data['color']]
                return True, (count, data['cost'] - count)
        return False, None


    def buy_railroad(self, edge, desired_color, cost):
        u, v, k, data = edge
        color, wild = cost
        A = self.node_map(u)
        B = self.node_map(v)
        discard = []
        while color > 0:
            i = self.resources.index(desired_color)
            discard.append(self.resources.pop(i))
        while wild > 0:
            i = self.resources.index(0)
            discard.append(self.resources.pop(i))
        self.trains -= self.G[A][B][k]['cost']
        # Merge nodes A, B in self.G, this will help find shortest paths
        self.G = nx.contracted_nodes(self.G, A, B, self_loops=False)
        self.node_map[v] = A
        return discard
        
    def count_resources(self):
        self.resource_count = {i:0 for i in range(9)}
        for resource in self.resources():
            self.resoucre_count[resource] += 1



