""" 
Linked list stack
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.head.data
    
    def isEmpty(self):
        return self.size == 0
    
    def getSize(self):
        return self.size
    
    def push(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.data

s = Stack()
s.push('A')
s.push('B')
s.push('C')

print("Pop: ", s.pop())
print("Peek: ", s.peek())
print("isEmpty: ", s.isEmpty())
print("Size: ", s.getSize())