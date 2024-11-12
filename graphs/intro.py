""" 
Graph Representations
Adjacency matrix and adjacency list will be our starting point
for creating graph representations
"""

# Adjacency matrix
vertexes = ['A', 'B', 'C', 'D'] # Vertex or node data

adjacency_matrix = [
    [0, 1, 1, 1],  # Edges for A
    [1, 0, 1, 0],  # Edges for B
    [1, 1, 0, 0],  # Edges for C
    [1, 0, 0, 0]   # Edges for D
]

def print_adjacency_matrix(matrix):
    print("\nAdjacency Matrix:")
    for row in matrix:
        print(row)

def print_connections(matrix, vertices):
    print("\nConnections:")
    for i in range(len(vertices)):
        print(f"{vertices[i]}: ", end="")
        for j in range(len(vertices)):
            if matrix[i][j]:  # if there is a connection
                print(vertices[j], end=" ")
        print()  # new line

print('vertexes:',vertexes)
print_adjacency_matrix(adjacency_matrix)
print_connections(adjacency_matrix, vertexes)

# Adjacency List
print("\nAdjacency List:")
V = 5   # Number of vertexes or nodes
edges = [[0, 1], [1, 2], [2, 0],[3, 1], [4, 0]]
adjacency_list = {}

# Add vertices to the dictionary
for i in range(V):
    adjacency_list[i] = []

# Add edges to the dictionary
for edge in edges:
    vertex1, vertex2 = edge
    adjacency_list[vertex1].append(vertex2)

# Display the adjacency list
for vertex, neighbors in adjacency_list.items():
    print(f"{vertex} -> {' '.join(map(str, neighbors))}")