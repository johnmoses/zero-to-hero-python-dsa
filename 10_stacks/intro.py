"""
Introducing Stacks
"""

from collections import deque


class Stack:
    """ 
    Initialize a stack and add some behavious
    """
    def __init__(self):
        self.data = deque()

    # Insert an element
    def push(self, val):
        self.data.append(val)

    # Check if empty
    def is_empty(self):
        return len(self.data) == 0

    # Get size
    def size(self):
        return len(self.data)

    # Get top item
    def top(self):
        return self.data[-1]

    # Delete an element
    def pop(self):
        return self.data.pop()

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.top())
print(s.size())
s.pop()
print(s.top())
print(s.size())