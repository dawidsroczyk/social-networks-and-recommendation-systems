# graphs/plotting/undirected_weighted_plotter.py
from .base_plotter import BaseGraphPlotter
import matplotlib.pyplot as plt

class UndirectedWeightedGraphPlotter(BaseGraphPlotter):
    def draw_edges(self, ax: plt.Axes) -> None:
        drawn = set()
        for u in self.graph.get_vertices():
            for v in self.graph.get_vertices():
                if (self.graph.has_edge(u, v) or self.graph.has_edge(v, u)):
                    edge = tuple(sorted((u, v)))
                    if edge in drawn:
                        continue

                    x1, y1 = self.graph.get_pos(edge[0])
                    x2, y2 = self.graph.get_pos(edge[1])
                    weight = self.graph.get_edge_attribute(edge[0], edge[1], "weight")
                    if weight is None:
                        weight = self.graph.get_edge_attribute(edge[1], edge[0], "weight") or 1

                    ax.plot([x1, x2], [y1, y2], color='green', linewidth=weight)

                    # Label weight at midpoint
                    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
                    ax.text(mx, my, f"{weight:.2f}", color='darkgreen', fontsize=8)

                    drawn.add(edge)
