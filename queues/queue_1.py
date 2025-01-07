""" 
Deque Queue
"""

from collections import deque

class Queue:
    def __init__(self):
        self.data = deque()

    def __len__(self):
        return len(self.data)

    # Get size
    def size(self):
        return len(self.data)

    # Check if empty
    def is_empty(self):
        return len(self.data) == 0

    def push(self, val):
        self.data.appendleft(val)

    def pop(self):
        return self.data.pop()

    # binary number support method
    def front(self):
        return self.data[-1]

if __name__ == "__main__":
    q = Queue()
    q.push(7)
    q.push(5)
    q.push(2)
    print('size: ', q.size())
    q.pop()
    if (q.is_empty() == False):
        print(q.front())
    q.pop()
    if (q.is_empty() == False):
        print(q.front())