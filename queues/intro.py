"""
Introduction to Queues
"""

class Queue:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    # Get size
    def size(self):
        return len(self.data)

    # Check if empty
    def is_empty(self):
        return len(self.data) == 0

    # Insert an element
    def push(self, x):
        if len(self.data) == 0:
            self.data.append(x)
            return
        tmp = self.data.pop(-1)
        self.push(x)
        self.data.append(tmp)

    # Remove and element
    def pop(self):
        return self.data.pop(-1)

    # Get front element
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
    