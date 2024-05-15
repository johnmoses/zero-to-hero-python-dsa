""" 
Deque Queue
"""

from collections import deque

class DequeQueue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        if len(self.buffer)==0:
            print("Queue is empty")
            return
        return len(self.buffer)==0

    def size(self):
        return len(self.buffer)

    # binary number support method
    def front(self):
        return self.buffer[-1]