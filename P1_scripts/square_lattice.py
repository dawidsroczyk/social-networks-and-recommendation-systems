import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from graphs.undirected import UndirectedGraph
from graphs.base import Node
from graphs.plotting.undirected_plotter import UndirectedGraphPlotter  # undirected graph plotter

def generate_square_lattice(rows: int, cols: int) -> UndirectedGraph:
    g = UndirectedGraph()
    # Add vertices with coordinates
    for r in range(rows):
        for c in range(cols):
            idx = r * cols + c
            g.add_vertex(Node(idx, x=c, y=-r))  # y = -r for positive y upwards in plot

    # Add undirected edges to right and bottom neighbors
    for r in range(rows):
        for c in range(cols):
            idx = r * cols + c
            if c < cols - 1:
                g.add_edge(idx, idx + 1)       # edge between current and right neighbor
            if r < rows - 1:
                g.add_edge(idx, idx + cols)    # edge between current and bottom neighbor
    return g

if __name__ == "__main__":
    lattice = generate_square_lattice(5, 5)
    plotter = UndirectedGraphPlotter(lattice)
    plotter.plot()
