from .base import Node
from .base import GraphBase
from typing import Dict, List, Tuple, Optional, Any, Set, FrozenSet
import random
import math
from tqdm import tqdm

class WeightedUndirectedGraph(GraphBase):
    def __init__(self):
        self.edges: Set[FrozenSet[int]] = set()
        self.nodes: Dict[int, Node] = {}
        self.edge_weights: Dict[FrozenSet[int], float] = {}

    def add_vertex(self, vertex: Node) -> None:
        if vertex.idx in self.nodes:
            raise ValueError(f"Vertex with index {vertex.idx} already exists.")
        self.nodes[vertex.idx] = vertex

    def add_edge(self, u: int, v: int, weight: float = 1.0) -> None:
        if u not in self.nodes:
            raise ValueError(f"Cannot add edge: vertex {u} does not exist.")
        if v not in self.nodes:
            raise ValueError(f"Cannot add edge: vertex {v} does not exist.")
        edge = frozenset({u, v})
        self.edges.add(edge)
        self.edge_weights[edge] = weight

    def has_edge(self, u: int, v: int) -> bool:
        return frozenset({u, v}) in self.edges

    def get_vertices(self) -> List[int]:
        return list(self.nodes.keys())

    def get_degree(self, vertex_idx: int) -> int:
        if vertex_idx not in self.nodes:
            raise ValueError(f"Vertex {vertex_idx} does not exist.")
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
        if attr_name == "weight":
            return self.edge_weights.get(frozenset({u, v}))
        return None

    def set_edge_attribute(self, u: int, v: int, attr_name: str, value: Any) -> None:
        if attr_name == "weight":
            edge = frozenset({u, v})
            if edge not in self.edge_weights:
                raise ValueError(f"Edge ({u}, {v}) does not exist.")
            self.edge_weights[edge] = float(value)
        else:
            raise ValueError(f"Unknown attribute '{attr_name}'")
    
    def optimize_layout(self, iterations: int = 50) -> None:
        """Automatically organize vertex positions for better visualization."""
        n = len(self.nodes)
        if n == 0:
            return
        
        for i in range(n):
            if self.nodes[i].x is None or self.nodes[i].y is None:
                self.set_pos(i, random.uniform(0, 100), random.uniform(0, 100))
        
        for iteration in tqdm(range(iterations)):
            for i in range(n):
                fx, fy = 0, 0
                x_i, y_i = self.get_pos(i)
                
                for j in range(n):
                    if i != j:
                        x_j, y_j = self.get_pos(j)
                        dx, dy = x_j - x_i, y_j - y_i
                        distance = math.sqrt(dx*dx + dy*dy) + 0.1
                        force = 200 / (distance * distance)
                        fx -= force * dx / distance
                        fy -= force * dy / distance
                
                for edge in self.edges:
                    if i in edge:
                        other = next(v for v in edge if v != i)
                        x_other, y_other = self.get_pos(other)
                        dx, dy = x_other - x_i, y_other - y_i
                        distance = math.sqrt(dx*dx + dy*dy) + 0.1
                        weight = self.edge_weights[edge]
                        force = distance * 0.05 * (weight / 10.0)
                        fx += force * dx / distance
                        fy += force * dy / distance
                
                cool = 1.0 - (iteration / iterations) * 0.9
                new_x = x_i + fx * cool * 0.1
                new_y = y_i + fy * cool * 0.1
                self.set_pos(i, max(5, min(95, new_x)), max(5, min(95, new_y)))
