"""
This AI was made to employ no randomness, 
if given the same circumstances, it should act the same every time
"""
from random import randint, choice
import networkx as nx
from Player import Player


class deterministicAI(Player):
    def __init__(self):
        super().__init__()
        self.desired_resources = {}

    def take_turn(self, actions, face_up):
        possible_actions = []
        self.count_resources()
        self.count_desired_resources()
        possible_buys = self.possible_resources(actions, face_up)
        if actions >= 2:
            if self.are_routes_finished():
                return 2, None  # Draw more routes
            elif len(possible_buys) > 0:
                possible_actions = self.possible_railroads()  # build railroads
            else:
                possible_actions = self.possible_resources(actions, face_up)
        else:
            possible_actions = self.possible_resources(actions, face_up)
        # print(possible_actions)
        return possible_actions[0]

    def possible_resources(self, actions, face_up):
        # What is it possible to draw?
        choices = [(0, 5)]
        if actions >= 2:
            choices.extend([(0, i) for i in range(5) if self.desired_resources[i] > 0])  # All face-up cards available
        else:
            choices.extend([(0, i) for i in range(5) if face_up[i] != 0 and self.desired_resources[i] > 0])
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
                    all_edges.extend([(a, b, k, self.G[a][b][k]['cost']/len(paths)) for k in range(num_paths)])
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
                # print("resource", self.resource_count)
                for color in range(1, 9):
                    if -cost <= self.desired_resources[color]:
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
        discard = [self.temp_routes.pop(route) for route in range(len(self.temp_routes)-1, -1, -1)]
        return discard

    def are_routes_finished(self):
        for route in self.routes:
            if len(self.railroads_along_route(route)) > 0:
                return False
        return True

    def count_desired_resources(self):
        self.desired_resources = {i: -self.resource_count[i] for i in range(9)}
        for route in self.routes:
            for railroad in self.railroads_along_route(route):
                u, v, k, cost = railroad
                self.desired_resources[self.G[u][v][k]['color']] += cost
        self.desired_resources[0] = 0
        # print("desired", self.desired_resources)
