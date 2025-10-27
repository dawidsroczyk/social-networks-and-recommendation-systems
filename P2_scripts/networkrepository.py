import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import random
from graphs.weighted_undirected import WeightedUndirectedGraph
from graphs.plotting.undirected_weighted_plotter import UndirectedWeightedGraphPlotter
from graphs.base import Node
import scipy.io
import numpy as np

matrix = scipy.io.mmread(os.path.join('P2_scripts', 'econ-mahindas.mtx'))
coo_matrix = matrix.tocoo()

edge_data = []
for i, j, weight in zip(coo_matrix.row, coo_matrix.col, coo_matrix.data):
    if i != j:
        edge_data.append([i, j, weight])

df_edge = pd.DataFrame(edge_data, columns=['source', 'target', 'weight'])

vertex_ids = sorted(set(df_edge['source']).union(set(df_edge['target'])))
vertex_labels = [f'Node_{id}' for id in vertex_ids]
df_vertex = pd.DataFrame({'Id': vertex_ids, 'Label': vertex_labels})

g = WeightedUndirectedGraph()

for idx, vertex_id in enumerate(vertex_ids):
    x = random.uniform(0, 100)
    y = random.uniform(0, 100)
    g.add_vertex(Node(idx, x, y))

for source, target, weight in df_edge.to_numpy():
    source_idx = vertex_ids.index(source)
    target_idx = vertex_ids.index(target)
    g.add_edge(source_idx, target_idx, weight)

g.optimize_layout()

vertex_mapper = {i: df_vertex.iloc[i]['Label'] for i in range(len(vertex_ids))}
plotter = UndirectedWeightedGraphPlotter(g, vertex_mapper)
plotter.plot(12, 10)