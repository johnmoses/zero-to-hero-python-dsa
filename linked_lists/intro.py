"""
Linked Lists
Starting with Singly Linked Lists
"""
class Node:
    def __init__(self, data=None):
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
firstNode = a
while firstNode:
    print(firstNode.data, end=" -> ")
    firstNode = firstNode.next
print('Null')
