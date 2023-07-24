# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 08:45:25 2023

@author: ASUS
"""

import numpy as np
from HyperRD.Hgraph import *

def simple_matrix(n: int, m: int, p: float) -> object:
    '''return a random hypergraph base on the generation of random incidence matrix'''
    random_matrix = np.zeros((n, m))
    for i in range(n):
        for j in range(m):
            if np.random.randint(1000, size=1)/1000 < p:
                random_matrix[i][j] = 1
    graph = Create()
    graph.vertices = set(range(n))
    graph.vertices_dict = graph.dict_of_vertices()
    for j in range(m):
        edge = []
        for i in range(n):
            if random_matrix[i][j] == 1:
                edge.append(i)
        graph.add_edge(edge)
    graph.inci_matrix = graph.incidence_matrix()
    return graph

def simple_bipartite(n: int, m: int, interation: int, p: float) -> object:
    '''return a random hypergraph base on the generation of bipartite graph'''
    edges = [set()]*m
    for k in range(interation):
        for i in range(n):
            edge_index = random.choice(range(m))
            edge = edges[edge_index].copy()
            if np.random.randint(1000, size=1)/1000 < p:
                edge.add(i)
                edges[edge_index] = edge
    graph = Create()
    graph.vertices = set(range(n))
    graph.vertices_dict = graph.dict_of_vertices()
    for j in range(m):
        graph.add_edge(edges[j])
    graph.inci_matrix = graph.incidence_matrix()
    return graph