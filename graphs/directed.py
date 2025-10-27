from .base import GraphBase
from .base import Node
from typing import Dict
from typing import List
from typing import Tuple
from typing import Optional
from typing import Any

class DirectedGraph(GraphBase):
    def __init__(self):
        self.edges: Set[Tuple[int, int]] = set()
        self.nodes: Dict[int, Node] = {}

    def add_vertex(self, vertex: Node) -> None:
        if vertex.idx in self.nodes:
            raise ValueError(f"Vertex with index {vertex.idx} already exists.")
        self.nodes[vertex.idx] = vertex

    def add_edge(self, from_idx: int, to_idx: int) -> None:
        if from_idx not in self.nodes:
            raise ValueError(f"Cannot add edge: vertex {from_idx} does not exist.")
        if to_idx not in self.nodes:
            raise ValueError(f"Cannot add edge: vertex {to_idx} does not exist.")
        self.edges.add((from_idx, to_idx))

    def has_edge(self, from_idx: int, to_idx: int) -> bool:
        return (from_idx, to_idx) in self.edges

    def get_vertices(self) -> List[int]:
        return list(self.nodes.keys())

    def get_degree(self, vertex_idx: int) -> int:
        if vertex_idx not in self.nodes:
            raise ValueError(f"Vertex {vertex_idx} does not exist.")
        return sum(1 for u, _ in self.edges if u == vertex_idx)

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
    
    def get_edge_attribute(self, from_idx: int, to_idx: int, attr_name: str) -> Optional[Any]:
        """Return attribute value for edge (from_idx, to_idx), or None if unsupported."""
        return None

    def set_edge_attribute(self, from_idx: int, to_idx: int, attr_name: str, value: Any) -> None:
        """Set attribute value for edge (from_idx, to_idx). Raises if unsupported."""
        raise NotImplementedError("Edge attributes not supported")