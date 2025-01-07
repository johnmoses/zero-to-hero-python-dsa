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

# Set first node
firstNode = a

# Traverse and display nodes in order
# There are many ways to do this

# while firstNode:
#     print(firstNode.data)
#     firstNode = firstNode.next

# nodes = ""
# while firstNode:
#     # print(firstNode.data)
#     nodes += (str(firstNode.data) + ' -> ')
#     firstNode = firstNode.next
# print(nodes)

nodes = []
while firstNode:
    nodes.append(firstNode.data)
    firstNode = firstNode.next
values = [str(i) + ' -> ' for i in nodes]
print(values)
