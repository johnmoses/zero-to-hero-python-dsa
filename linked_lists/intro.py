"""
Linked Lists

Starting with Singly Linked Lists
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Instantiate Node
a = Node(20)
b = Node(30)
c = Node(40)

# Link the nodes
a.next = b
b.next = c

# Traverse and display nodes in order

# Method 1
# Set first node as current
current = a
while current:
    print(current.data, end=' -> ')
    current = current.next
print()

# Method 2
# Set first node as current
current = a
nodes = ""
while current:
    nodes += (str(current.data) + ' -> ')
    current = current.next
print(nodes)

# Method 3
# Set first node as current
current = a
nodes = []
while current:
    nodes.append(current.data)
    current = current.next
values = [str(i) + ' -> ' for i in nodes]
print(values)
