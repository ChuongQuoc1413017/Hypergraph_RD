# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 19:50:30 2023

@author: ASUS
"""

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