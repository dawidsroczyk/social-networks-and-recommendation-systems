# graphs/plotting/directed_weighted_plotter.py
from .base_plotter import BaseGraphPlotter
import matplotlib.pyplot as plt

class DirectedWeightedGraphPlotter(BaseGraphPlotter):
    def draw_edges(self, ax: plt.Axes) -> None:
        for from_idx in self.graph.get_vertices():
            for to_idx in self.graph.get_vertices():
                if self.graph.has_edge(from_idx, to_idx):
                    x1, y1 = self.graph.get_pos(from_idx)
                    x2, y2 = self.graph.get_pos(to_idx)
                    weight = self.graph.get_edge_attribute(from_idx, to_idx, "weight") or 1

                    dx = x2 - x1
                    dy = y2 - y1
                    ax.arrow(
                        x1, y1, dx * 0.85, dy * 0.85,
                        head_width=0.1 * weight, head_length=0.1 * weight,
                        length_includes_head=True,
                        fc='blue', ec='blue',
                        linewidth=weight
                    )

                    # Label weight at edge midpoint
                    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
                    ax.text(mx, my, f"{weight:.2f}", color='navy', fontsize=8)
