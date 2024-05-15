"""
Introduction to Queues
"""

class Queue:
    def __init__(self):
        self.data = []

    # Insert an element
    def enQueue(self, x):
        if len(self.data) == 0:
            self.data.append(x)
            return
        tmp = self.data.pop(-1)
        self.enQueue(x)
        self.data.append(tmp)

    # Remove and element
    def deQueue(self):
        return self.data.pop(-1)

    # Get front element
    def front(self):
        return self.data[-1]

    # Check if empty
    def isEmpty(self):
        return len(self.data) == 0

q = Queue()
print("queue")
q.enQueue(5)
q.enQueue(3)
q.deQueue()
if (q.isEmpty() == False):
    print(q.front())
q.deQueue()
if (q.isEmpty() == False):
    print(q.front())
    