""" 
Deque stack
"""

from collections import deque

class DequeStack:
    def __init__(self):
        self.data = deque()

    def __len__(self):
        return len(self.data)

    def size(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data)==0
    
    def push(self,val):
        self.data.append(val)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

if __name__ == "__main__":
    s = DequeStack()

    s.push(5)
    s.push(9)
    s.push(34)
    s.push(78)
    s.push(12)
    print(s.size())