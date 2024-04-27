"""
Linked List
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

if __name__ == "__main__":
    print('Linked List')
    ll = LinkedList()