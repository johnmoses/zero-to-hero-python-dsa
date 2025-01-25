""" 
Queue implementation with deque library
"""

from collections import deque

class Queue:
    def __init__(self):
        self.data = deque()

    def __len__(self):
        return len(self.data)

    def getSize(self):
        return len(self.data)

    def isEmpty(self):
        return len(self.data) == 0

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.data[0]

    # binary number support method
    def front(self):
        return self.data[-1]

    def enqueue(self, element):
        self.data.append(element)
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.data.pop()

q = Queue()

q.enqueue('A')
q.enqueue('B')
q.enqueue('C')
print("Dequeue: ", q.dequeue())
print("Peek: ", q.peek())
print("isEmpty: ", q.isEmpty())
print("Size: ", q.getSize())