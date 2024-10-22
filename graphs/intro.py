"""
Breadth-first-search Graph
"""

def breadth_first_search(graph: dict, start: str) -> set[str]:
    """
    Join sorted strings
    """
    explored = {start}
    queue = [start]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            explored.add(w)
            queue.append(w)
    return explored

G = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}
print(breadth_first_search(G, "A"))