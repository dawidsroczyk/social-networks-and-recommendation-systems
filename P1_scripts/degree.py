import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from graphs.weighted_undirected import WeightedUndirectedGraph
from graphs.base import Node
from graphs.plotting.undirected_weighted_plotter import UndirectedWeightedGraphPlotter

def generate_random_weighted_undirected_graph(num_nodes: int, edge_probability: float = 0.3) -> WeightedUndirectedGraph:
    g = WeightedUndirectedGraph()

    # Randomly position nodes within a 10x10 square
    for i in range(num_nodes):
        x = random.uniform(0, 10)
        y = random.uniform(0, 10)
        g.add_vertex(Node(i, x=x, y=y))

    # Randomly add edges with given probability
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if random.random() < edge_probability:
                g.add_edge(i, j)
                weight = round(random.uniform(0.1, 5.0), 2)
                g.set_edge_attribute(i, j, 'weight', weight)

    return g

if __name__ == "__main__":
    random_graph = generate_random_weighted_undirected_graph(15, edge_probability=0.25)

    # Create vertex labels as "idx: degree"
    vertex_labels = {
        idx: f"{idx}: {random_graph.get_degree(idx)}"
        for idx in random_graph.get_vertices()
    }

    plotter = UndirectedWeightedGraphPlotter(random_graph, vertex_mapper=vertex_labels)
    plotter.plot()
