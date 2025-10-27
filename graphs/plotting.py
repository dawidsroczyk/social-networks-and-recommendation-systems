import matplotlib.pyplot as plt
from .base import Node, GraphBase
from typing import Dict

def plot_graph(graph: GraphBase, vertex_mapper: Dict[int, str] = None) -> None:
    fig, ax = plt.subplots()
    
    # Plot vertices
    for vertex_idx in graph.get_vertices():
        try:
            x, y = graph.get_pos(vertex_idx)
        except ValueError as e:
            raise ValueError(f"Cannot plot graph: {e}")

        ax.plot(x, y, 'o', color='skyblue', markersize=10)

        label = vertex_mapper[vertex_idx] if vertex_mapper and vertex_idx in vertex_mapper else str(vertex_idx)
        ax.text(x + 0.05, y + 0.05, label, fontsize=12)

    # Plot edges
    for from_idx in graph.get_vertices():
        for to_idx in graph.get_vertices():
            if graph.has_edge(from_idx, to_idx):
                try:
                    x1, y1 = graph.get_pos(from_idx)
                    x2, y2 = graph.get_pos(to_idx)
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

    ax.set_aspect('equal')
    ax.axis('off')
    plt.tight_layout()
    plt.show()
