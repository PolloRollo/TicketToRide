"""
"""
from random import randint, choice
import networkx as nx
from Player import Player


class RandomAI(Player):
    def take_turn(self, actions, face_up):
        possible_actions = []
        if actions >= 2:
            # build railroad
            possible_actions.extend(self.possible_railroads())
            # draw destinations
            possible_actions.extend([(2, None)])
        possible_actions.extend(self.possible_resources(actions, face_up))
        # print(possible_actions)
        return choice(possible_actions)

    def possible_resources(self, actions, face_up):
        # What is it possible to draw?
        choices = [(0, top) for top in range(5, 10)]
        if actions >= 2:
            choices.extend([(0, i) for i in range(5)])  # All face-up cards available
        else:
            choices.extend([(0, i) for i in range(5) if face_up[i] != 0])
        return choices

    def possible_railroads(self):
        # Where is it possible to build?
        possible_edges = []
        for route in self.routes:
            possible_edges.extend(self.railroads_along_route(route))

        buyable_railroads = self.buyable_railroads(possible_edges)
        return buyable_railroads

    def railroads_along_route(self, route):
        all_edges = []
        A, B = route.get_destinations()
        A = self.node_map[A]
        B = self.node_map[B]
        if nx.has_path(self.G, A, B):
            paths = [p for p in nx.all_shortest_paths(self.G, source=A, target=B, weight='cost')]
            for path in paths:
                for i in range(1, len(path)):
                    num_paths = len(self.G[path[i-1]][path[i]])
                    # print("num_paths", num_paths)
                    a = path[i-1]
                    b = path[i]
                    all_edges.extend([(a, b, k, self.G[a][b][k]['cost']) for k in range(num_paths)])
        return all_edges

    def buyable_railroads(self, edges):
        buyable_railroads = []
        for edge in edges:
            u, v, k, cost = edge

            if self.G[u][v][k]['color'] != 0:
                buyable, desired_color = self.check_can_buy(edge, self.G[u][v][k]['color'])
                if buyable:
                    edge_id = self.G[u][v][k]['edge_id']
                    buyable_railroads.append((1, (self.edge_map[edge_id], self.G[u][v][k]['color'])))
            else:
                for color in range(1, 9):
                    buyable, desired_color = self.check_can_buy(edge, color)
                    if buyable:
                        edge_id = self.G[u][v][k]['edge_id']
                        buyable_railroads.append((1, (self.edge_map[edge_id], desired_color)))
        return buyable_railroads

    def get_resource(self, resource):
        self.resources.append(resource)

    def choose_routes(self, min=1):
        for i in range(min):
            chosen_route = randint(0, len(self.temp_routes) - 1)
            self.routes.append(self.temp_routes.pop(chosen_route))
        discard = [route for route in self.temp_routes]
        self.temp_routes = []
        return discard
