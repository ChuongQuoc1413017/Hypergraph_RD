# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 08:45:25 2023

@author: ASUS
"""

import numpy as np
import random
import itertools 
from HyperRD.Hgraph import *

def simple_matrix(n: int, m: int, p: float) -> object:
    '''return a random hypergraph based on the generation of random incidence matrix'''
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
    '''return a random hypergraph based on the generation of bipartite graph'''
    edges = [set()]*m
    for k in range(interation):
        edge_index = random.choice(range(m))
        edge = edges[edge_index].copy()
        for i in range(n):
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

def simple_powersets(n: int, p: float) -> object:
    '''return a random hypergraph based on the generation of powerset'''
    def powerset(iterable):
        "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
        s = list(iterable)
        return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))
    
    edges = []
    edges_possible = list(powerset(list(range(n))))
    for edge in edges_possible:
        if np.random.randint(1000, size=1)/1000 < p:
            edges.append(edge)
    graph = Create()
    graph.vertices = set(range(n))
    graph.vertices_dict = graph.dict_of_vertices()
    for edge in edges:
        graph.add_edge(edge)
    graph.inci_matrix = graph.incidence_matrix()
    return graph

def k_uniform(n: int, k: int, p: float) -> object:
    '''return a k-uniform random hypergraph'''
    edges = []
    edges_possible = [i for i in itertools.combinations(range(n), k)]
    for edge in edges_possible:
        if np.random.randint(1000, size=1)/1000 < p:
            edges.append(edge)
    graph = Create()
    graph.vertices = set(range(n))
    graph.vertices_dict = graph.dict_of_vertices()
    for edge in edges:
        graph.add_edge(edge)
    graph.inci_matrix = graph.incidence_matrix()
    return graph