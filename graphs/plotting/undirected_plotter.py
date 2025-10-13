import matplotlib.pyplot as plt
from graphs.base import GraphBase
from typing import Optional, Dict

class UndirectedGraphPlotter:
    def __init__(self, graph: GraphBase, vertex_mapper: Optional[Dict[int, str]] = None):
        self.graph = graph
        self.vertex_mapper = vertex_mapper

    def plot(self) -> None:
        fig, ax = plt.subplots()

        # Plot vertices
        for vertex_idx in self.graph.get_vertices():
            try:
                x, y = self.graph.get_pos(vertex_idx)
            except ValueError as e:
                raise ValueError(f"Cannot plot graph: {e}")

            ax.plot(x, y, 'o', color='skyblue', markersize=10)

            label = self.vertex_mapper[vertex_idx] if self.vertex_mapper and vertex_idx in self.vertex_mapper else str(vertex_idx)
            ax.text(x + 0.05, y + 0.05, label, fontsize=12)

        # Plot edges (undirected, so draw line once per edge)
        edges_drawn = set()
        for from_idx in self.graph.get_vertices():
            for to_idx in self.graph.get_vertices():
                if from_idx == to_idx:
                    continue
                if self.graph.has_edge(from_idx, to_idx) or self.graph.has_edge(to_idx, from_idx):
                    # To avoid drawing duplicate edges in undirected graph:
                    edge = tuple(sorted((from_idx, to_idx)))
                    if edge in edges_drawn:
                        continue
                    edges_drawn.add(edge)

                    try:
                        x1, y1 = self.graph.get_pos(from_idx)
                        x2, y2 = self.graph.get_pos(to_idx)
                    except ValueError as e:
                        raise ValueError(f"Cannot plot edge between {from_idx} and {to_idx}: {e}")

                    ax.plot([x1, x2], [y1, y2], color='gray', linewidth=1)

        ax.set_aspect('equal')
        ax.axis('off')
        plt.tight_layout()
        plt.show()
