import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from graphs.undirected import UndirectedGraph
from graphs.base import Node
from graphs.plotting.undirected_plotter import UndirectedGraphPlotter

def generate_cycle_graph(length: int) -> UndirectedGraph:
    g = UndirectedGraph()
    # Add vertices in a circle with coordinates on a circle for better visualization
    import math
    radius = 5
    for i in range(length):
        angle = 2 * math.pi * i / length
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        g.add_vertex(Node(i, x=x, y=y))

    # Add edges connecting each node to the next
    for i in range(length):
        g.add_edge(i, (i + 1) % length)  # last connects to first to close the cycle

    return g

if __name__ == "__main__":
    cycle = generate_cycle_graph(10)
    plotter = UndirectedGraphPlotter(cycle)
    plotter.plot()
