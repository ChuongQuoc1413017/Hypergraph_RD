# Hypergraph_RD
Python package for Random and Dynamical Hypergraph Computation

## Library Requirement
`random`, `itertools`, `numpy`, `networkx` (in the future)

## Structure
- `Hgraph`: store all `class` objects
  - `Hgraph.Create`: undirected hypergraph object, including the following features and methods:
    - Features:
        - `vertices`: python set of vertices
        - `vertices_dict`: python dictionary of vertices
        - `vertices_weight`: python list of vertex weights **(still developed)**
        - `edges`: python set of hyperedges
        - `edges_dict`: python dictionary of hyperedges
        - `edges_weight`: python list of hyperedge weights **(still developed)**
        - `inci_matrix`: numpy matrix of an incidence matrix representation
    - Methods:
        - `add_vertex()`: add a vertex
        - `add_edge()`: add a hyperedge
        - `dict_of_vertices()`: return vertices in terms of an encoded dictionary
        - `dict_of_edges()`: return hyperedges in terms of an encoded dictionary
        - `degree_vertex()`: return degree of a vertex
        - `degree_edge()`: return degree of a hyperedge
        - `diag_vertex()`: return a numpy diagonal matrix of vertex degrees
        - `diag_edge()`: return a numpy diagonal matrix of hyperedge degrees
        - `remove_vertex()`: remove a vertex
        - `remove_edge()`: remove a hyperedge
        - `incidence_matrix()`: calculate an incidence matrix and store this matrix in `inci_matrix`
  - `Hgraph.Create_Normal`: undirected normal graph object, including the following features and methods:
    - Features:
        - `vertices`: number of vertices
        - `adj`: adjacency list of graph
    - Methods:
        - `add_edge()`: add edge
        - `dfs_utility()`: depth-first search algorithm to traverse the graph
        - `connected_components()`: return list of connected components
