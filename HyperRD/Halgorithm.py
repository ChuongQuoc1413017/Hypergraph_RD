# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 19:50:30 2023

@author: ASUS
"""

from HyperRD.Hgraph import *
import itertools

def vertex_connected(graph: object, start: object, end: object) -> bool:
    '''check whether two vertices are connected'''
    keys = list(graph.vertices)
    keys.sort()
    values = [False] * len(keys)
    visited = {k: v for k, v in zip(keys, values)}
    edges = graph.edges
    
    # Create a queue for BFS
    queue = []

    # Mark the source node as
    # visited and enqueue it
    queue.append(start)
    visited[start] = True

    while queue:

        # Dequeue a vertex from
        # queue and print it
        point = queue.pop(0)

        # Get all adjacent vertices of the
        # dequeued vertex s.
        # If an adjacent has not been visited,
        # then mark it visited and enqueue it
        for edge in edges:
            if point in edge:
                for vertex in edge:
                    if visited[vertex] == False:
                        queue.append(vertex)
                        visited[vertex] = True
                    if visited[end] == True:
                        return True
    return False

def graph_connected(graph: object) -> bool:
    '''check whether a graph is connected'''
    vertices = list(graph.vertices)
    for u in vertices:
        for v in vertices:
            if u != v:
                if not vertex_connected(graph, u, v):
                    return False
    return True

def components_connected(graph: object) -> list:
    '''return list of connected components'''
    vertices = graph.vertices_dict
    edges = graph.edges_dict
    vertices_length = len(vertices)
    edges_length = len(edges)
    normal_graph = Create_Normal(vertices_length + edges_length)
    
    for vertex in range(vertices_length):
        for edge in range(edges_length):
            if vertices[vertex] in edges[edge]:
                normal_graph.add_edge(vertex, edge + vertices_length)
            
    cc = normal_graph.connected_components()
    components = []
    for cluster in cc:
        component = []
        for i in cluster:
            if i < vertices_length:
                component.append(vertices[i])
        components.append(component)
        
    return components

def simple_reduction(graph: object) -> object:
    '''reduce hypergraph to simple hypergraph'''
    graph_new = graph.copy()
    edge_list = list(graph.edges)
    for i in range(len(edge_list)):
        for j in range(len(edge_list)):
            if i != j and edge_list[j].issubset(edge_list[i]):
                edge_list_new = list(graph_new.edges)
                if edge_list[j] in edge_list_new:
                    graph_new.remove_edge(edge_list[j])
    return graph_new

def graph_expansion(graph: object, mode: str) -> object:
    '''expand hypergraph to normal graph'''
    vertices = graph.vertices_dict
    vertices_swap = {v: k for k, v in vertices.items()}
    edges = graph.edges_dict
    vertices_length = len(vertices)
    edges_length = len(edges)
    if mode == 'clique':
        g = Create_Normal(vertices_length)
        for edge in range(edges_length):
            for i in itertools.combinations(edges[edge], 2):
                g.add_edge(vertices_swap[i[0]], vertices_swap[i[1]])
    elif mode == 'star':
        g = Create_Normal(vertices_length + edges_length)
        for edge in range(edges_length):
            for i in edges[edge]:
                g.add_edge(edge + vertices_length, vertices_swap[i])
    return g