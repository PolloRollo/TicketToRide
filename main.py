import networkx as nx
from math import log
import matplotlib.pyplot as plt
import os


def main(n):
    G = nx.MultiGraph()
    G = nx.generators.erdos_renyi_graph(n, (log(n) + 1)/n)
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos=pos, with_labels=True, font_weight='bold')
    plt.show()
    
    edge_data = [('color', int), ('cost', int)]
    H = nx.read_edgelist("defaultMap.txt", delimiter=', ', data=edge_data, create_using=nx.MultiGraph)
    pos = nx.spring_layout(H)
    nx.draw_networkx(H, pos=pos, with_labels=True, font_weight='bold')
    plt.show()
    # plt.savefig("path.png")


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


def get_American_map():
    G = nx.MultiGraph()
    list = [(1, 2, {"length": 6, "color": 2}),
            (1, 2, {"length": 6, "color": 4})]
    return G

def get_America_routes():
    destinations = [
        Destination("Dallas", "New York", 11),
        Destination("Portland", "Phoenix", 11),
        Destination("Vancouver", "Santa Fe", 13),
        Destination("Seattle", "New York", 22),
        Destination("Montreal", "Atlanta", 9),
        Destination("Toronto", "Miami", 10),
        Destination("Boston", "Miami", 12),
        Destination("Los Angeles", "Chicago", 16),
        Destination("Winnipeg", "Houston", 12),
        Destination("Denver", "El Paso", 4),
        Destination("Duluth", "Houston", 8),
        Destination("San Francisco", "Atlanta", 17),
        Destination("Denver", "Pittsburgh", 11),
        Destination("Sault St. Marie", "Nashville", 8),
        Destination("Winnipeg", "Little Rock", 11),
        Destination("Duluth", "El Paso", 10),
        Destination("Seattle", "Los Angeles", 9),
        Destination("Helena", "Los Angeles", 8),
        Destination("Kansas City", "Houston", 5),
        Destination("Sault St. Marie", "Oklahoma City", 9),
        Destination("Portland", "Nashville", 17),
        Destination("Los Angeles", "New York", 21),
        Destination("Chicago", "Santa Fe", 9),
        Destination("Calgary", "Phoenix", 13),
        Destination("Calgary", "Salt Lake City", 7),
        Destination("Vancouver", "Montreal", 20),
        Destination("Los Angeles", "Miami", 20),
        Destination("Chicago", "New Orleans", 7),
        Destination("New York", "Atlanta", 6),
        Destination("Montreal", "New Orleans", 13)
    ]
    return destinations


def convert(file):
    if not os.access(file, 0):
        print("Error: Failed to access graph file")
    f = open(file)

    color_dict = {"Colors.none": 0,
                  "Colors.red": 1,
                  "Colors.orange": 2,
                  "Colors.yellow": 3,
                  "Colors.green": 4,
                  "Colors.blue": 5,
                  "Colors.pink": 6,
                  "Colors.white": 7,
                  "Colors.black": 8}
    G = nx.MultiGraph()
    edges = []
    for line in f:
        a = line.split()
        b = []
        if len(a) > 0:
            a[0] = a[0][5:]
            a[-2] = a[-2][-2:]
            a[-1] = str(color_dict[a[-1][6:-2]])

        a = " ".join(a)
        b = a.split(", ")
        c = (b[0][1:-1], b[1][1:-1], {"cost": int(b[2]), "color": int(b[3])})
        edges.append(c)
        # print(b)
        # print(c)
    f.close()
    G.add_edges_from(edges)


    nx.write_edgelist(G, "defaultMap.txt", delimiter= ', ', data=['color', 'cost'])
    edge_data = [('color', int), ('cost', int)]
    H = nx.read_edgelist("defaultMap.txt", delimiter=', ', data=edge_data, create_using=nx.MultiGraph)
    pos = nx.spring_layout(H)
    nx.draw_networkx(H, pos=pos, with_labels=True, font_weight='bold')
    plt.show()
    print(H.edges)


convert("americamap.txt")
#main(25)