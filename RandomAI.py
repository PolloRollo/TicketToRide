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
        print(possible_actions)
        return choice(possible_actions)

    def possible_resources(self, actions, face_up):
        # What is it possible to draw?
        choices = [(0, 5)]
        if actions >= 2:
            choices.extend([(0, i) for i in range(5)])  # All face-up cards available
        else:
            choices.extend([(0, i) for i in range(5) if face_up[i] != 0])
        return choices

    def possible_railroads(self):
        # Where is it possible to build?
        possible_edges = []
        for route in self.routes:
            A, B = route.get_destinations()
            if nx.has_path(self.G, A, B):
                print([p for p in nx.all_shortest_paths(self.G, source=A, target=B, weight='cost')])
        # (1, details)
        # details = (edge, resources)?
        return [(0, 5)]

    def get_resource(self, resource):
        self.resources.append(resource)

    def choose_routes(self, min=1):
        for i in range(min):
            chosen_route = randint(0, len(self.temp_routes)-1)
            self.routes.append(self.temp_routes.pop(chosen_route))
        discard = [route for route in self.temp_routes]
        self.temp_routes = []
        return discard