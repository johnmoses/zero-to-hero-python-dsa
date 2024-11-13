""" 
Undirected Graph with adjacency matrix representation
"""
class Graph:
    def __init__(self, size):
        self.edges = [[0] * size for _ in range(size)]
        self.size = size
        self.nodes = [''] * size  

    # Edges in the matrix
    def add_edge(self, u, v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.edges[u][v] = 1
            self.edges[v][u] = 1

    # Nodes or vertices
    def add_node(self, node, data):
        if 0 <= node < self.size:
            self.nodes[node] = data

    def print_graph(self):
        print("\nEdges:")
        for row in self.edges:
            print(' '.join(map(str, row)))
        print("\nNodes:")
        for node, data in enumerate(self.nodes):
            print(f"Node {node}: {data}")

g = Graph(4)
g.add_node(0, 'A')
g.add_node(1, 'B')
g.add_node(2, 'C')
g.add_node(3, 'D')
g.add_edge(0, 1)  # A - B
g.add_edge(0, 2)  # A - C
g.add_edge(0, 3)  # A - D
g.add_edge(1, 2)  # B - C

g.print_graph()