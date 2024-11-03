"""
Basic binary tree
"""

class Node:
    """ 
    Node with value variable and pointers to nodes
    """
    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Node | None = None
        self.right: Node | None = None

class BinaryTree:
    """
    Implementation
    """
    target: int

    def __init__(self) -> None:
        self.paths = 0

tree = Node(10)
tree.left = Node(5)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)
print(tree.left)