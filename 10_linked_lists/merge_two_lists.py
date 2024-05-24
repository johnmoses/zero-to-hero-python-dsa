"""
Merge Two Lists
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_two_lists(l1: Node, l2: Node) -> Node:
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.data < l2.data:
        l1.next = merge_two_lists(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_lists(l1, l2.next)
        return l2
    
l1 = [1,2,4]
l2 = [1,3,4]
print(merge_two_lists(Node(l1), Node(l2)))