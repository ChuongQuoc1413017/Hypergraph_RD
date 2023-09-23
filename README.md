# Hypergraph_RD
Python package for Random and Dynamical Hypergraph Computation

## Library Requirement
- mandatory: `random`, `itertools`, `numpy`
- optional: `networkx`, `hypernetx`

## Structure
- `HyperRD.Hgraph`: store all `class` objects
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
        - `degree_vertex()`: return a degree of a vertex
        - `degree_edge()`: return a degree of a hyperedge
        - `diag_vertex()`: return a numpy diagonal matrix of vertex degrees
        - `diag_edge()`: return a numpy diagonal matrix of hyperedge degrees
        - `remove_vertex()`: remove a vertex
        - `remove_edge()`: remove a hyperedge
        - `incidence_matrix()`: calculate an incidence matrix and store this matrix in `inci_matrix`
        - `copy()`: make a copy of graph
  - `Hgraph.Create_Normal`: undirected normal graph object, including the following features and methods:
    - Features:
        - `vertices`: number of vertices
        - `adj`: adjacency list of graph
    - Methods:
        - `add_edge()`: add edge
        - `dfs_utility()`: depth-first search algorithm to traverse the graph
        - `connected_components()`: return a list of connected components
        - `copy()`: make a copy of graph
  - `Hgraph.Multilayer`: multilayer hypergraph object, including the following features and methods:
    - Features:
      - `layers`: list of hypergraphs
      - `interlink`: set of interlinking hyperedge
    - Methods:
      - `add_graph()`: add layer
      - `add_interlink()`: add interlinking hyperedge
      - `number_of_layer`: return number of layers
## Analyze tools
- `HyperRD.Halgorithm`: tools to analyze hypergraphs
  - `vertex_connected()`: check if two vertices are connected
  - `graph_connected()`: check if a hypergraph is fully connected
  - `components_connected()`: return a list of connected components in the hypergraph
  - `simple_reduction()`: reduce hypergraph to simple hypergraph (has no repeated hyperedge)
  - `graph_expansion()`: expand a hypergraph to a normal graph, based on *chapter 2* of this book [Hypergraph Computation](https://link.springer.com/book/10.1007/978-981-99-0185-2)
    - `mode == 'clique'`: clique expansion
    - `mode == 'star'`: star expansion or birpartite equivalence
    - `mode == 'line'`: line expansion **(still developed)**
## Random hypergraph generator
- `HyperRD.Hrandom`: generate random hypergraphs
  - `simple_matrix()`: each element of an incidence matrix will be set value *1* randomly with probability *p* **(uniform distribution)**
  - `simple_bipartite()`: create a random hypergraph with probability *p*, based on this paper **(uniform distribution)**
  - `simple_powersets()`: create a random hypergraph with probability *p*, based on the random choice of all possible edges (power set of vertices) **(uniform distribution)**
  - `k_uniform()`: create a k-uniform hypergraph with probability *p*, based on this paper **(uniform distribution)**
## Stochastic processes on hypergraph
- `HyperRD.Hdynamic`: analyze stochastic processes on hypergraph
  - `transit_prob_matrix()`: return a uniform transition probability matrix of hypergraph (simple random walk)
## Switch to other platforms
- `HyperRD.Htranslate`: change to other platforms (check the optional section of library requirement)
  - `hyperrd_to_networkx()`: switch from `Hgraph.Create_Normal` object to [`NetworkX`](https://networkx.org/documentation/stable/index.html) object
  - `hyperrd_to_hypernetx()`: switch from `Hgraph.Create` object to [`HyperNetX`](https://pnnl.github.io/HyperNetX) object
