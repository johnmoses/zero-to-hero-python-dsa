"""
Basic binary tree
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

a = Node("A")   # Root
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
g = Node("G")

a.left = b
a.right = c

b.left = d
b.right = e

c.left = f
c.right = g

# Test
print("a.right.left.data:", a.right.left.data)