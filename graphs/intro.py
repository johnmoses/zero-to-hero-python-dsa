"""
Basic graph
"""

from collections import deque

def _input(message):
    return input(message).strip().split(" ")

def initialize_unweighted_directed_graph(
    node_count: int, edge_count: int
) -> dict[int, list[int]]:
    graph: dict[int, list[int]] = {}
    for i in range(node_count):
        graph[i + 1] = []

    for e in range(edge_count):
        x, y = (int(i) for i in _input(f"Edge {e + 1}: <node1> <node2> "))
        graph[x].append(y)
    return graph

if __name__ == "__main__":
    n, m = (int(i) for i in _input("Number of nodes and edges: "))

    graph_choice = int(
        _input(
            "Press 1 or 2 or 3 \n"
            "1. Unweighted directed \n"
            "2. Unweighted undirected \n"
            "3. Weighted undirected \n"
        )[0]
    )

    g = {
        1: initialize_unweighted_directed_graph,
        2: initialize_unweighted_undirected_graph,
        3: initialize_weighted_undirected_graph,
    }[graph_choice](n, m)