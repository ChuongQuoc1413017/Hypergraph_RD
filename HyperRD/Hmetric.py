# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 19:50:30 2023

@author: ASUS
"""

from HyperRD.Hgraph import *

def density(graph: object) -> float:
    '''return the density of hypergraph:
       density = (the number of edges) / (the number of possible edges)'''
    return len(graph.edges) / (2**len(graph.vertices) - 1)

def girth(graph: object) -> int:
    '''return the size of the smallest non-empty hyperedge in the hypergraph'''
    return min(len(edge) for edge in graph.edges)

def average_vertex_degree(graph: object) -> float:
    graph.incidence_matrix()
    '''return the average degree across all vertices in the hypergraph'''
    total_degree = [graph.degree_vertex(graph.dict_of_vertices()[vertex]) for vertex in range(len(graph.vertices))]
    return sum(total_degree) / len(total_degree)

def average_edge_size(graph: object) -> float:
    '''return the average size across all edges in the hypergraph'''
    total_size = [len(edge) for edge in graph.edges]
    return sum(total_size) / len(total_size)