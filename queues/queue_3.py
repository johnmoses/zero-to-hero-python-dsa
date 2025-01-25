""" 
Linked list implementation
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
    
    def isEmpty(self):
        return self.length == 0
    
    def getSize(self):
        return self.length
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.front.data
    
    def enqueue(self, element):
        new_node = Node(element)
        if self.rear is None:
            self.front = self.rear = new_node
            self.length += 1
            return
        self.rear.next = new_node
        self.rear = new_node
        self.length += 1
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        temp = self.front
        self.front = temp.next
        self.length -= 1
        if self.front is None:
            self.rear = None
        return temp.data

    def printQueue(self):
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

q = Queue()

q.enqueue('A')
q.enqueue('B')
q.enqueue('C')
print("Queue: ", end="")
q.printQueue()
print("Dequeue: ", q.dequeue())
print("Peek: ", q.peek())
print("isEmpty: ", q.isEmpty())
print("Size: ", q.getSize())
