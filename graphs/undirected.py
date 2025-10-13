from .base import GraphBase, Node
from typing import Dict, List, Tuple, Optional, Any, Set, FrozenSet

class UndirectedGraph(GraphBase):
    def __init__(self):
        self.edges: Set[FrozenSet[int]] = set()  # edges stored as unordered sets of node indices
        self.nodes: Dict[int, Node] = {}

    def add_vertex(self, vertex: Node) -> None:
        if vertex.idx in self.nodes:
            raise ValueError(f"Vertex with index {vertex.idx} already exists.")
        self.nodes[vertex.idx] = vertex

    def add_edge(self, u: int, v: int) -> None:
        if u not in self.nodes:
            raise ValueError(f"Cannot add edge: vertex {u} does not exist.")
        if v not in self.nodes:
            raise ValueError(f"Cannot add edge: vertex {v} does not exist.")
        self.edges.add(frozenset({u, v}))

    def has_edge(self, u: int, v: int) -> bool:
        return frozenset({u, v}) in self.edges

    def get_vertices(self) -> List[int]:
        return list(self.nodes.keys())

    def get_degree(self, vertex_idx: int) -> int:
        if vertex_idx not in self.nodes:
            raise ValueError(f"Vertex {vertex_idx} does not exist.")
        # Count edges that contain the vertex
        return sum(1 for edge in self.edges if vertex_idx in edge)

    def get_pos(self, vertex_idx: int) -> Tuple[float, float]:
        if vertex_idx not in self.nodes:
            raise ValueError(f"Vertex {vertex_idx} does not exist.")
        node = self.nodes[vertex_idx]
        if node.x is None or node.y is None:
            raise ValueError(f"Position for vertex {vertex_idx} is not set.")
        return (node.x, node.y)

    def set_pos(self, vertex_idx: int, x: float, y: float) -> None:
        if vertex_idx not in self.nodes:
            raise ValueError(f"Cannot set position: vertex {vertex_idx} does not exist.")
        self.nodes[vertex_idx].x = x
        self.nodes[vertex_idx].y = y

    def get_edge_attribute(self, u: int, v: int, attr_name: str) -> Optional[Any]:
        # No edge attributes supported by default
        return None

    def set_edge_attribute(self, u: int, v: int, attr_name: str, value: Any) -> None:
        raise NotImplementedError("Edge attributes not supported")
