""" 
Graph Representations
Adjacency matrix is a good starting point for creating graph representations
"""

nodes = ['A', 'B', 'C', 'D'] # Vertex or node data

edges = [
    [0, 1, 1, 1],  # Edges for A
    [1, 0, 1, 0],  # Edges for B
    [1, 1, 0, 0],  # Edges for C
    [1, 0, 0, 0]   # Edges for D
]

# Adjacency matrix
def print_edges(edges):
    print("\nEdges:")
    for row in edges:
        print(row)

def print_connections(edges, nodes):
    print("\nConnections:")
    for i in range(len(nodes)):
        print(f"{nodes[i]}: ", end="")
        for j in range(len(nodes)):
            if edges[i][j]:  # if there is a connection
                print(nodes[j], end=" ")
        print()  # new line

print('Nodes:',nodes)
print_edges(edges)
print_connections(edges, nodes)
