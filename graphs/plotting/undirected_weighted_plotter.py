# graphs/plotting/undirected_weighted_plotter.py
from .base_plotter import BaseGraphPlotter
import matplotlib.pyplot as plt
import numpy as np


class UndirectedWeightedGraphPlotter(BaseGraphPlotter):
    def draw_edges(self, ax: plt.Axes) -> None:
        drawn = set()
        weights = []

        for u in self.graph.get_vertices():
            for v in self.graph.get_vertices():
                if self.graph.has_edge(u, v) or self.graph.has_edge(v, u):
                    edge = tuple(sorted((u, v)))
                    if edge in drawn:
                        continue
                    drawn.add(edge)
                    w = (
                        self.graph.get_edge_attribute(u, v, "weight")
                        or self.graph.get_edge_attribute(v, u, "weight")
                        or 1
                    )
                    weights.append(w)

        if not weights:
            return

        w_min, w_max = min(weights), max(weights)
        drawn.clear()

        for u in self.graph.get_vertices():
            for v in self.graph.get_vertices():
                if self.graph.has_edge(u, v) or self.graph.has_edge(v, u):
                    edge = tuple(sorted((u, v)))
                    if edge in drawn:
                        continue
                    drawn.add(edge)

                    x1, y1 = self.graph.get_pos(edge[0])
                    x2, y2 = self.graph.get_pos(edge[1])
                    weight = (
                        self.graph.get_edge_attribute(edge[0], edge[1], "weight")
                        or self.graph.get_edge_attribute(edge[1], edge[0], "weight")
                        or 1
                    )

                    if w_max > w_min:
                        norm_w = (weight - w_min) / (w_max - w_min)
                    else:
                        norm_w = 0.5

                    color = plt.cm.Greens(0.3 + 0.7 * norm_w)
                    linewidth = 1 + 2 * norm_w
                    alpha = 0.3 + 0.7 * norm_w

                    ax.plot(
                        [x1, x2],
                        [y1, y2],
                        color=color,
                        linewidth=linewidth,
                        alpha=alpha,
                        zorder=1,
                    )

                    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
                    offset = 0.02
                    dx, dy = x2 - x1, y2 - y1
                    length = np.hypot(dx, dy)
                    if length > 0:
                        nx, ny = -dy / length, dx / length
                        mx += offset * nx
                        my += offset * ny
                    '''
                    ax.text(
                        mx,
                        my,
                        f"{weight:.2f}",
                        color="black" if norm_w > 0.5 else "darkgreen",
                        fontsize=8,
                        ha="center",
                        va="center",
                        zorder=2,
                        bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.6),
                    )
                    '''
