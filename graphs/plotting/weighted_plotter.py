import matplotlib.pyplot as plt
from .base_plotter import BaseGraphPlotter
from typing import Any

class WeightedGraphPlotter(BaseGraphPlotter):
    def draw_edges(self, ax: plt.Axes) -> None:
        for from_idx in self.graph.get_vertices():
            for to_idx in self.graph.get_vertices():
                if self.graph.has_edge(from_idx, to_idx):
                    try:
                        x1, y1 = self.graph.get_pos(from_idx)
                        x2, y2 = self.graph.get_pos(to_idx)
                        weight = self.graph.get_edge_attribute(from_idx, to_idx, "weight")
                    except ValueError as e:
                        raise ValueError(f"Cannot plot edge from {from_idx} to {to_idx}: {e}")

                    if weight is None:
                        weight = 1  # default weight if none

                    ax.plot([x1, x2], [y1, y2], color='gray', linewidth=weight)

                    # Optionally display the weight as text
                    mid_x = (x1 + x2) / 2
                    mid_y = (y1 + y2) / 2
                    ax.text(mid_x, mid_y, f"{weight:.2f}", color='red', fontsize=8)
