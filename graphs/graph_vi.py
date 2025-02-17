""" 
Adjacency list graph representation
"""

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