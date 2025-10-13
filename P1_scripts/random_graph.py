import sys
import os
import random
import math

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from graphs.weighted_undirected import WeightedUndirectedGraph
from graphs.base import Node
from graphs.plotting.undirected_weighted_plotter import UndirectedWeightedGraphPlotter

def generate_less_chaotic_weighted_undirected_graph(num_nodes: int, max_edges_per_node: int = 2) -> WeightedUndirectedGraph:
    g = WeightedUndirectedGraph()

    # Place nodes evenly on a circle for nice layout
    radius = 10
    for i in range(num_nodes):
        angle = 2 * math.pi * i / num_nodes
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        g.add_vertex(Node(i, x=x, y=y))

    # Add edges: for each node, add edges to random other nodes (undirected)
    # To avoid duplicates, keep track of added edges
    added_edges = set()

    for i in range(num_nodes):
        possible_targets = [n for n in range(num_nodes) if n != i and (min(i, n), max(i, n)) not in added_edges]
        targets = random.sample(possible_targets, min(max_edges_per_node, len(possible_targets)))

        for t in targets:
            weight = round(random.uniform(0.5, 3.0), 2)
            g.add_edge(i, t)
            g.set_edge_attribute(i, t, 'weight', weight)
            added_edges.add((min(i, t), max(i, t)))

    return g

if __name__ == "__main__":
    random_graph = generate_less_chaotic_weighted_undirected_graph(10, max_edges_per_node=2)
    plotter = UndirectedWeightedGraphPlotter(random_graph)
    plotter.plot()
