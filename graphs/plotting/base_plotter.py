import matplotlib.pyplot as plt
from abc import ABC, abstractmethod
from typing import Dict, Optional
from ..base import GraphBase

class BaseGraphPlotter(ABC):
    def __init__(self, graph: GraphBase, vertex_mapper: Optional[Dict[int, str]] = None):
        self.graph = graph
        self.vertex_mapper = vertex_mapper or {}

    def draw_nodes(self, ax: plt.Axes) -> None:
        for v in self.graph.get_vertices():
            x, y = self.graph.get_pos(v)
            ax.plot(x, y, 'o', color='skyblue', markersize=10)
            label = self.vertex_mapper.get(v, str(v))
            ax.text(
                x + 0.07, y + 0.07, label,
                fontsize=8,
                fontweight='bold',
                ha='left', va='bottom',
                bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='none', alpha=0.7)
            )


    @abstractmethod
    def draw_edges(self, ax: plt.Axes) -> None:
        """Must be implemented by subclasses to draw edges with custom styles"""

    def plot(self, width=10, height=8) -> None:
        fig, ax = plt.subplots(figsize=(width, height))
        self.draw_edges(ax)
        self.draw_nodes(ax)
        ax.set_aspect('equal')
        ax.axis('off')
        plt.tight_layout()
        plt.show()