from .directed import DirectedGraph
from .base import Node
from typing import Optional, Any, Tuple

class WeightedDirectedGraph(DirectedGraph):
    def __init__(self):
        super().__init__()
        # Store weights keyed by (from_idx, to_idx)
        self.edge_weights: dict[Tuple[int, int], float] = {}

    def add_edge(self, from_idx: int, to_idx: int, weight: float = 1.0) -> None:
        super().add_edge(from_idx, to_idx)
        self.edge_weights[(from_idx, to_idx)] = weight

    def get_edge_attribute(self, from_idx: int, to_idx: int, attr_name: str) -> Optional[Any]:
        if attr_name == "weight":
            return self.edge_weights.get((from_idx, to_idx))
        return None

    def set_edge_attribute(self, from_idx: int, to_idx: int, attr_name: str, value: Any) -> None:
        if attr_name == "weight":
            if (from_idx, to_idx) not in self.edge_weights:
                raise ValueError(f"Edge ({from_idx}, {to_idx}) does not exist.")
            self.edge_weights[(from_idx, to_idx)] = float(value)
        else:
            raise ValueError(f"Unknown attribute '{attr_name}'")
