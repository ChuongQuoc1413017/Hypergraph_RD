# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 08:45:26 2023

@author: ASUS
"""
import numpy as np
from HyperRD.Hgraph import *

def transit_prob_matrix(graph_input: object, lazy = False) -> np.matrix:
    '''return a uniform transition probability matrix of hypergraph'''
    graph = graph_input.copy()
    if len(graph.inci_matrix) == 0:
        graph.inci_matrix = graph.incidence_matrix()
    edge_matrix = np.matmul(graph.inci_matrix.transpose(), graph.inci_matrix)
    adj_matrix = np.matmul(graph.inci_matrix, graph.inci_matrix.transpose())
    edge_matrix_diag = np.diag(np.diag(edge_matrix))
    if lazy == True:
        degree_matrix = np.matmul(graph.inci_matrix, np.matmul(edge_matrix_diag, graph.inci_matrix.transpose()))
    else:
        degree_matrix = np.matmul(graph.inci_matrix, np.matmul(edge_matrix_diag, graph.inci_matrix.transpose())) - adj_matrix
        degree_matrix = degree_matrix - np.diag(np.diag(degree_matrix))
    n = degree_matrix.shape[0]
    for i in range(n):
        degree_matrix[i, :] /= np.sum(degree_matrix[i, :])
    return degree_matrix