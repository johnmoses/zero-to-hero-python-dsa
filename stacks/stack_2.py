""" 
Deque stack
"""

from collections import deque

class Stack:
    def __init__(self):
        self.data = deque()

    def __len__(self):
        return len(self.data)

    def getSize(self):
        return len(self.data)

    def isEmpty(self):
        return len(self.data)==0

    def top(self):
        return self.data[-1]
    
    def push(self,val):
        self.data.append(val)

    def pop(self):
        return self.data.pop()

if __name__ == "__main__":
    s = Stack()

    s.push(5)
    s.push(9)
    s.push(34)
    s.push(78)
    s.push(12)
    print(s.getSize())