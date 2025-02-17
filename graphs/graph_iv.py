""" 
Graph
"""

class Node:
    """ 
    Node represent each vertex of the graph
    data: stored data or value
    edges: list of edges representing connections
    """
    def __init__(self, data, edges=None):
        self.data = data
        if edges is None:
            self.edges = []
        else:
            self.edges = edges

    def add_edge(self, edge):
        self.edges.append(edge)

    def __str__(self):
        res = f"{self.data}"
        res += "None"
        return res

class Graph:
    """
    Main graph data structure 
    """
    def __init__(self, nodes=None):
        if nodes is None:
            self.nodes = []
        else:
            self.nodes = nodes

    def add_node(self, data, edges=None):
        """ 
        Add new named node to the graph
        """
        self.nodes.append(Node(data, edges))

    def find_node(self, data):
        """ 
        Search for nodes
        """
        for node in self.nodes:
            if node.data == data:
                return node
        return None

    def add_edge(self, node_from, node_to, weight=1):
        """
        Add new edge between two nodes
        """
        node_1 = self.find_node(node_from)
        node_2 = self.find_node(node_to)
        if (node_1 is not None) and (node_2 is not None):
            node_1.add_edge((node_1, weight))
            node_2.add_edge((node_2, weight))
        else:
            print("Sorry, one or more nodes were not found")

    def print_graph(self):
        print("\nConnections:")
        for i in range(len(self.nodes)):
            print(f"{self.nodes[i]}: ", end="")
            for j in range(len(self.nodes)):
                # if self.nodes.edges[i][j]:
                print(self.nodes[j], end=" ")
            print()

    def __str__(self):
        graph = ""
        for node in self.nodes:
            graph += f"{node.__str__()}\n"
        return graph

g = Graph()

# Add nodes
g.add_node("John")
g.add_node("Mary")

# Add edges
g.add_edge("John", "Mary")
g.print_graph()