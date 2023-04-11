"""
"""
import networkx as nx
from math import log
import matplotlib.pyplot as plt
# import matplotlib.colormaps


class Map:
    def __init__(self, G, player_count):
        # G is a map with weightings for length and color, Multigraph
        self.G = G
        self.player_count = player_count

        # Functions
        self.label_all_unclaimed()

    def get_edges(self, data, keys):
        return self.G.edges(data=data, keys=keys)
    
    def label_all_unclaimed(self):
        for u, v, k in self.G.edges(keys=True):
            self.G[u][v][k]['claimed_by'] = None
            
    def claim_edge(self, player, edge):
        # claim route for player
        u, v, k = edge
        self.G[u][v][k]['claimed_by'] = player.player_id
        if self.player_count <= 3:
            if len(self.G[u][v]) > 1:
                for extra, details in self.G[u][v].items():
                    if extra != k:
                        self.G[u][v][extra]['claimed_by'] = -1

    def get_weight(self, edge):
        return 0

    def get_color(self, edge):
        return 0

    def display_map(self):
        claimed = []
        unclaimed = []
        color_map = []
        
        for u, v, k, d in self.G.edges(keys=True, data='claimed_by'):
            if d is None or d == -1:
                unclaimed.append((u, v, k))
            else:
                color_map.append(d)
                claimed.append((u, v, k))

        corners = {'Vancouver': [[-.9, .9]],
                   'Boston': [[.9, .9]],
                   'Los Angeles': [[-.9, -.9]],
                   'Miami': [[.9, -.9]]}
        # fixed = ['Vancouver', 'Boston', 'Los Angeles', 'Miami']
        pos = nx.spring_layout(self.G, pos=corners)
        cmap = plt.cm.rainbow

        plt.figure(figsize=(11, 8))
        nx.draw_networkx(self.G, pos=pos, with_labels=True)
        nx.draw_networkx_edges(self.G, pos=pos, edgelist=unclaimed, width=1, style='-.')
        nx.draw_networkx_edges(self.G, pos=pos, edgelist=claimed, edge_color=color_map, edge_cmap=cmap, width=5)
        plt.title('Ticket To Ride: America')
        plt.savefig("test_map.png", dpi=150)
        plt.show()

