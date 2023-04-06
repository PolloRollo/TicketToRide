"""
"""
import networkx as nx
from math import log
import matplotlib.pyplot as plt


class Map:
    def __init__(self, G, player_count):
        # G is a map with weightings for length and color, Multigraph
        self.G = G
        self.player_count = player_count

        # Functions
        self.label_all_unclaimed()

    def all_edges(self):
        return self.G.edges(data=True, keys=True)
    
    def label_all_unclaimed(self):
        for u, v, k in self.G.edges(keys=True):
            self.G[u][v][k]['claimed_by'] = None
            
    def claim_edge(self, player, edge):
        # claim route for player
        if self.player_count <= 3:
            print("0")
            #if players <= 3, other route claimed inaccessable
        return 0

    def get_weight(self, edge):
        return 0

    def get_color(self, edge):
        return 0

