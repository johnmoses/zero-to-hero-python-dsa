""" 
Traverse singly-linked list
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverse_and_print(head):
    node = head
    while node:
        print(node.data, end=" -> ")
        node = node.next
    print("null")

a = Node(20)
b = Node(30)
c = Node(40)
d = Node(10)
e = Node(70)

a.next = b
b.next = c
c.next = d
d.next = e

traverse_and_print(a)