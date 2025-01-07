"""
Array Stack
"""

class Stack:
    """ 
    Initialize a stack and add some behavious
    """
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    # Get size
    def getSize(self):
        return len(self.data)

    # Check if empty
    def isEmpty(self):
        return len(self.data) == 0

    # Get top or peek item
    def top(self):
        return self.data[-1]

    # Insert an element
    def push(self, val):
        self.data.append(val)

    # Remove an element
    def pop(self):
        return self.data.pop()

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print('Size: ', s.getSize())
print('Pop: ', s.pop())
print('Top: ', s.top())
print('Size: ', s.getSize())