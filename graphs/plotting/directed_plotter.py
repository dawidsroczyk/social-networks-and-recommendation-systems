import matplotlib.pyplot as plt
from .base_plotter import BaseGraphPlotter

class DirectedGraphPlotter(BaseGraphPlotter):
    def draw_edges(self, ax: plt.Axes) -> None:
        for from_idx in self.graph.get_vertices():
            for to_idx in self.graph.get_vertices():
                if self.graph.has_edge(from_idx, to_idx):
                    try:
                        x1, y1 = self.graph.get_pos(from_idx)
                        x2, y2 = self.graph.get_pos(to_idx)
                    except ValueError as e:
                        raise ValueError(f"Cannot plot edge from {from_idx} to {to_idx}: {e}")

                    dx = x2 - x1
                    dy = y2 - y1

                    ax.arrow(
                        x1, y1, dx * 0.85, dy * 0.85,
                        head_width=0.1, head_length=0.1,
                        length_includes_head=True,
                        fc='gray', ec='gray'
                    )
