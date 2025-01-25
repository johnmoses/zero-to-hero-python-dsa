"""
Binary Tree
"""

class Node:
    def __init__(self, data, left=None, right=None):
        """
        Create a node (vertex) of the tree
        """
        self.data = data
        self.left = left
        self.right = right

    def set_child(self, branch, child):
        """
        Add a child node as left or right child to the current node
        branch : str
        child : Node
        """
        if branch == "left":
            self.left = child
        else:
            self.right = child

    def __str__(self):
        return str(self.data)

  

class Tree:
  """
    Create a new tree
    root : Node
  """
  def __init__(self, root):
    self.root = root

  def preorder(self, node):
    """
      Generate the preorder traverse of the tree
      node : Node
      Returns preorder traversal
    """
    if node:
      print(node, end=" ")
      self.preorder(node.left)
      self.preorder(node.right)


  def inorder(self, node):
    """
      Generate the inroder traverse of the tree
      node : Node
      Returns inorder traversal
    """
    if node:
      self.inorder(node.left)
      print(node, end=" ")
      self.inorder(node.right)


  def postorder(self, node):
    """
      Generate the postorder traverse of the tree
      node : Node
      Returns postorder traversal
    """
    if node:
      self.postorder(node.left)
      self.postorder(node.right)
      print(node, end=" ")
      
# Create the nodes of the tree
a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")

# Set the hierarchy between the nodes
a.set_child("left", b)
a.set_child("right", c)

b.set_child("left", d)
b.set_child("right", e)

c.set_child("right", f)

# Creata the tree setting up the root node
tree = Tree(a)

# Execute the traversal
print("Preorder Traversal")
tree.preorder(a)
print("\n")

print("Inorder Traversal")
tree.inorder(a)
print("\n")

print("Postorder Traversal")
tree.postorder(a)