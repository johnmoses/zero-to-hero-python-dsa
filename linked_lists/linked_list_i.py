"""
Simplified Singly Linked List class
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        if self.head is None:
            node = Node(data)
            self.head = node
            self.tail = node
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
        return self.tail
        
    def printList(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

ll = LinkedList()
ll.add(10)
ll.add(20)
ll.add(30)
ll.printList()