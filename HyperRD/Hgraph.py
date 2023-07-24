# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 19:46:14 2023

@author: ASUS
"""

import numpy as np

class Create(object):
    
    def __init__(self):
        
        # For vertices
        self.vertices = set()
        self.vertices_dict = {}
        self.vertices_weight = []
        
        # For edges
        self.edges = set()
        self.edges_dict = {}
        self.edges_weight = []
        
        # For representation
        self.inci_matrix = None
        
    def add_edge(self: object, edge: list) -> None:
        '''add edge'''
        if set(edge) != set():
            edge = frozenset(edge)
            (self.edges).add(edge)
            for vertex in edge:
                (self.vertices).add(vertex)
            self.vertices_dict = self.dict_of_vertices()
            self.edges_dict = self.dict_of_edges()
    
    def add_vertex(self: object, vertex: object) -> None:
        '''add vertex'''
        (self.vertices).add(vertex)
        self.vertices_dict = self.dict_of_vertices()
            
    def dict_of_vertices(self: object) -> dict:
        '''return list of vertices in term of Python dictionary'''
        keys = range(len(self.vertices))
        values = list(self.vertices)
        values.sort()
        vertices_dict = {k: v for k, v in zip(keys, values)}
        return vertices_dict
        
    def dict_of_edges(self: object) -> dict:
        '''return list of edges in term of Python dictionary'''
        keys = range(len(self.edges))
        values = self.edges
        edges_dict = {k: v for k, v in zip(keys, values)}
        return edges_dict
        
    def incidence_matrix(self: object) -> np.matrix:
        '''return incidence matrix of graph'''
        vertices_dict = self.vertices_dict
        edges_dict =  self.edges_dict
        inci_matrix = np.zeros((len(vertices_dict), len(edges_dict)))
        for i in range(len(vertices_dict)):
            for j in range(len(edges_dict)):
                if vertices_dict[i] in edges_dict[j]:
                    inci_matrix[i][j] = 1
        self.inci_matrix = np.matrix(inci_matrix)
        return self.inci_matrix

    def degree_vertex(self: object, vertex: object) -> float:
        '''return degree of vertex'''
        vertices_dict = self.vertices_dict
        if vertex not in self.vertices:
            return 0.
        else:
            key = list(filter(lambda x: vertices_dict[x] == vertex, vertices_dict))[0]
            return np.sum((self.inci_matrix)[key, :])

    def degree_edge(self: object, edge: set) -> float:
        '''return degree of edge'''
        edge_dict = self.edges_dict
        if edge not in self.edges:
            return 0.
        else:
            key = list(filter(lambda x: edge_dict[x] == edge, edge_dict))[0]
            return np.sum((self.inci_matrix)[:, key])
        
    def diag_vertex(self: object) -> np.matrix:
        '''return a diagonal matrix of vertex degrees'''
        return np.matrix(np.diag([self.degree_vertex(self.vertices_dict[i]) for i in range(len(self.vertices_dict))]))
    
    def diag_edge(self: object) -> np.matrix:
        '''return a diagonal matrix of edge degree'''
        return np.matrix(np.diag([self.degree_edge(self.edges_dict[i]) for i in range(len(self.edges_dict))]))
    
    def remove_vertex(self: object, vertex: object) -> None:
        '''remove vertex from graph'''
        (self.vertices).remove(vertex)
        old_edges = self.edges
        if frozenset([vertex]) in old_edges:
            (self.edges).remove(frozenset([vertex]))
        new_edges = set()
        for edge in old_edges:
            new_edges.add(edge.difference(frozenset([vertex])))
        self.edges = new_edges
        
        self.vertices_dict = self.dict_of_vertices()
        self.edges_dict = self.dict_of_edges()
        
    def remove_edge(self: object, edge: object) -> None:
        '''remove edge from graph'''
        (self.edges).remove(frozenset(edge))
        self.edges_dict = self.dict_of_edges()