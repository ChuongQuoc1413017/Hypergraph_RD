# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 19:46:14 2023

@author: ASUS
"""

import numpy as np

class Create(object):
    
    # init function to declare class variables
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
        
    def add_vertex(self: object, vertex: object) -> None:
        '''add vertex'''
        (self.vertices).add(vertex)
        self.vertices_dict = self.dict_of_vertices()
        
    def add_edge(self: object, edge: list) -> None:
        '''add edge'''
        if set(edge) != set():
            edge = frozenset(edge)
            (self.edges).add(edge)
            for vertex in edge:
                (self.vertices).add(vertex)
            self.vertices_dict = self.dict_of_vertices()
            self.edges_dict = self.dict_of_edges()
            
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
        
class Create_Normal(object):
 
    # init function to declare class variables
    def __init__(self, vertices):
        
        # represent graph as adjacency list
        self.vertices = vertices
        self.adj = [[] for i in range(vertices)]
        
    def add_edge(self: object, start: int, end: int) -> None:
        '''add edge'''
        self.adj[start].append(end)
        self.adj[end].append(start)
 
    def dfs_utility(self: object, temp: list, vertex: int, visited: list) -> list:
        '''Depth-first search algorithm'''
        # Mark the current vertex as visited
        visited[vertex] = True
 
        # Store the vertex to list
        temp.append(vertex)
 
        # Repeat for all vertices adjacent
        # to this vertex v
        for i in self.adj[vertex]:
            if visited[i] == False:
 
                # Update the list
                temp = self.dfs_utility(temp, i, visited)
        return temp
 
    # Method to retrieve connected components
    # in an undirected graph
    def connected_components(self: object) -> list:
        '''return list of connected components'''
        visited = []
        components = []
        for i in range(self.vertices):
            visited.append(False)
        for vertex in range(self.vertices):
            if visited[vertex] == False:
                temp = []
                components.append(self.dfs_utility(temp, vertex, visited))
        return components