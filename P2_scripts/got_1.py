import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import random
from graphs.weighted_undirected import WeightedUndirectedGraph
from graphs.plotting.undirected_weighted_plotter import UndirectedWeightedGraphPlotter
from graphs.base import Node
import math
import random

edge_path = os.path.join('P2_scripts', 'got-s1-edges.csv')
vertex_path = os.path.join('P2_scripts', 'got-s1-nodes.csv')

df_edge = pd.read_csv(edge_path)
df_vertex = pd.read_csv(vertex_path)

g = WeightedUndirectedGraph()
n = df_vertex.shape[0]
for i in range(n):
    x = random.uniform(0, 100)
    y = random.uniform(0, 100)
    g.add_vertex(Node(i, x, y))

for source, target, weight, _ in df_edge.to_numpy():
    try:
        source_idx = df_vertex['Id'].to_list().index(source)
        target_idx = df_vertex['Id'].to_list().index(target)
        g.add_edge(source_idx, target_idx, weight)
    except Exception as e:
        print(f'Got error when creating graph: {e}')
        continue

g = WeightedUndirectedGraph()
n = df_vertex.shape[0]
for i in range(n):
    x = random.uniform(0, 100)
    y = random.uniform(0, 100)
    g.add_vertex(Node(i, x, y))

for source, target, weight, _ in df_edge.to_numpy():
    try:
        source_idx = df_vertex['Id'].to_list().index(source)
        target_idx = df_vertex['Id'].to_list().index(target)
        g.add_edge(source_idx, target_idx, weight)
    except Exception as e:
        print(f'Got error when creating graph: {e}')
        continue

g.optimize_layout()

vertex_mapper = {i: df_vertex.iloc[i]['Label'] for i in range(n)}
plotter = UndirectedWeightedGraphPlotter(g, vertex_mapper)
plotter.plot(10, 8)