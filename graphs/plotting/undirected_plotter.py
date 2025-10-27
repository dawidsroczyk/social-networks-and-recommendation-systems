import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
from graphs.base import GraphBase
from typing import Optional, Dict
from tqdm import tqdm

class UndirectedGraphPlotter:
    def __init__(self, graph: GraphBase, vertex_mapper: Optional[Dict[int, str]] = None):
        self.graph = graph
        self.vertex_mapper = vertex_mapper

    def plot(self) -> None:
        fig, ax = plt.subplots()

        for vertex_idx in self.graph.get_vertices():
            try:
                x, y = self.graph.get_pos(vertex_idx)
            except ValueError as e:
                raise ValueError(f"Cannot plot graph: {e}")

            ax.plot(x, y, 'o', color='skyblue', markersize=10)

            label = self.vertex_mapper[vertex_idx] if self.vertex_mapper and vertex_idx in self.vertex_mapper else str(vertex_idx)
            ax.text(x + 0.05, y + 0.05, label, fontsize=12)

        edges_drawn = set()
        for from_idx in self.graph.get_vertices():
            for to_idx in self.graph.get_vertices():
                if from_idx == to_idx:
                    continue
                if self.graph.has_edge(from_idx, to_idx) or self.graph.has_edge(to_idx, from_idx):
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

    def spring_energy(self, positions):
        energy = 0.0
        vertices = self.graph.get_vertices()
        
        for i in range(len(vertices)):
            for j in range(i + 1, len(vertices)):
                pos_i = positions[vertices[i]]
                pos_j = positions[vertices[j]]
                dx = pos_i[0] - pos_j[0]
                dy = pos_i[1] - pos_j[1]
                dist = np.sqrt(dx*dx + dy*dy) + 1e-8
                energy += 1.0 / (dist * dist)
        
        for u in vertices:
            for v in vertices:
                if self.graph.has_edge(u, v):
                    pos1 = positions[u]
                    pos2 = positions[v]
                    dx = pos1[0] - pos2[0]
                    dy = pos1[1] - pos2[1]
                    dist = np.sqrt(dx*dx + dy*dy)
                    energy += 0.5 * (dist - 1.0) ** 2
        
        return energy

    def draw_configuration(self, positions, ax):
        ax.clear()
        for v, pos in positions.items():
            ax.scatter(pos[0], pos[1], s=100, c='lightblue', edgecolors='black')
            ax.text(pos[0], pos[1], str(v), ha='center', va='center', fontsize=8)
        
        for u in positions:
            for v in positions:
                if self.graph.has_edge(u, v):
                    x1, y1 = positions[u]
                    x2, y2 = positions[v]
                    ax.plot([x1, x2], [y1, y2], 'gray', alpha=0.6)
        
        ax.set_xlim(-1, 11)
        ax.set_ylim(-1, 11)
        ax.set_aspect('equal')

    def simulated_annealing(self, iterations=50000):
        vertices = self.graph.get_vertices()
        
        current_positions = {}
        for v in vertices:
            x, y = self.graph.get_pos(v)
            current_positions[v] = np.array([x, y])
        
        current_energy = self.spring_energy(current_positions)
        temperature = 100.0
        
        positions_history = [current_positions.copy()]
        
        for iteration in tqdm(range(iterations)):
            new_positions = current_positions.copy()
            node_to_move = np.random.choice(vertices)
            old_pos = new_positions[node_to_move].copy()
            new_positions[node_to_move] = old_pos + np.random.normal(0, 0.2, 2)
            
            new_energy = self.spring_energy(new_positions)
            delta_energy = new_energy - current_energy
            
            if delta_energy < 0 or np.random.random() < np.exp(-delta_energy / temperature):
                current_positions = new_positions
                current_energy = new_energy
            
            temperature *= 0.95
            
            if iteration % 2000 == 0:
                positions_history.append(current_positions.copy())
        
        for v, pos in current_positions.items():
            self.graph.set_pos(v, pos[0], pos[1])
        
        return positions_history

    def prepare_animation(self, positions_history, filename=None):
        fig, ax = plt.subplots(figsize=(8, 8))
        
        def animate(frame):
            self.draw_configuration(positions_history[frame], ax)
            ax.set_title(f'Iteration {frame * 2000}')
        
        anim = animation.FuncAnimation(fig, animate, frames=len(positions_history), interval=200)
        
        if filename:
            anim.save(filename, writer='pillow', fps=5)
        
        plt.show()
        return anim

    def spring_layout_workflow(self, animation_filename=None):
        vertices = self.graph.get_vertices()
        
        initial_positions = {}
        for v in vertices:
            x = np.random.uniform(0, 10)
            y = np.random.uniform(0, 10)
            self.graph.set_pos(v, x, y)
            initial_positions[v] = np.array([x, y])
        
        fig, ax = plt.subplots(figsize=(8, 8))
        self.draw_configuration(initial_positions, ax)
        ax.set_title('Initial Random Configuration')
        plt.show()
        
        positions_history = self.simulated_annealing()
        
        anim = self.prepare_animation(positions_history, animation_filename)
        
        fig, ax = plt.subplots(figsize=(8, 8))
        final_positions = positions_history[-1]
        self.draw_configuration(final_positions, ax)
        ax.set_title('Final Configuration')
        plt.show()
        
        return anim