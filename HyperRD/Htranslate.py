# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 08:45:26 2023

@author: ASUS
"""

import networkx as nx

def hyperrd_to_networkx(graph: object) -> object:
    G = nx.Graph()
    for i in range(graph.vertices):
        G.add_node(i)
    edge = graph.adj
    for i in range(graph.vertices):
        for j in edge[i]:
            G.add_edge(i, j)
    return G