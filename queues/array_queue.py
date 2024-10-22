""" 
Array Queue
"""

class ArrayQueue(object):
    def __init__(self):
        self.data = []

    def push(self, x):
        if len(self.data) == 0:
            self.data.append(x)
            return
        tmp = self.data.pop(-1)
        self.push(x)
        self.data.append(tmp)

    def pop(self):
        return self.data.pop(-1)

    def peek(self):
        return self.data[-1]

    def empty(self):
        return len(self.data) == 0

if __main__ == "__main__":
    data = ["ArrayQueue", "push", "push", "peek", "pop", "empty"]
    sn = ArrayQueue()
    sn.push(5)
    sn.push(3)
    print(sn)