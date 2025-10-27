from abc import ABC
from abc import abstractmethod
from typing import List
from typing import Optional
from typing import Any

class Node:
    def __init__(self, idx: int, x: float = None, y: float = None):
        self.idx = idx
        self.x = x
        self.y = y
        self.attributes = {}

    def __hash__(self):
        return hash(self.idx)

    def __eq__(self, other):
        return isinstance(other, Node) and self.idx == other.idx

    def __repr__(self):
        return f"Node(idx={self.idx}, x={self.x}, y={self.y})"


class GraphBase(ABC):

    @abstractmethod
    def add_edge(self, from_idx: int, to_idx: int) -> None:
        pass
    
    @abstractmethod
    def has_edge(self, from_idx: int, to_idx: int) -> bool:
        pass
    
    @abstractmethod
    def get_vertices(self) -> List[int]:
        pass
    
    @abstractmethod
    def add_vertex(self, vertex: Node):
        pass
    
    @abstractmethod
    def get_degree(self, vertex_idx: int) -> int:
        pass
    
    @abstractmethod
    def get_pos(self, vertex_idx: int) -> (float, float):
        pass
    
    @abstractmethod
    def set_pos(self, vertex_idx: int, x: float, y: float) -> None:
        pass
    
    @abstractmethod
    def get_edge_attribute(self, from_idx: int, to_idx: int, attr_name: str) -> Optional[Any]:
        """Return attribute value for edge (from_idx, to_idx), or None if unsupported."""
        pass

    @abstractmethod
    def set_edge_attribute(self, from_idx: int, to_idx: int, attr_name: str, value: Any) -> None:
        """Set attribute value for edge (from_idx, to_idx). Raises if unsupported."""
        pass