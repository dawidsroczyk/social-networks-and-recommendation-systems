import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from graphs.undirected import UndirectedGraph
from graphs.base import Node
from graphs.plotting.undirected_plotter import UndirectedGraphPlotter

def generate_complete_graph(n: int) -> UndirectedGraph:
    g = UndirectedGraph()

    # Place nodes evenly on a circle for better visualization
    import math
    radius = 5
    for i in range(n):
        angle = 2 * math.pi * i / n
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        g.add_vertex(Node(i, x=x, y=y))

    # Add edges between every pair of distinct nodes
    for i in range(n):
        for j in range(i + 1, n):
            g.add_edge(i, j)

    return g

if __name__ == "__main__":
    complete = generate_complete_graph(8)
    plotter = UndirectedGraphPlotter(complete)
    plotter.plot()
