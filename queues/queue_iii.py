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
    
    # Get size
    def getSize(self):
        return self.length
    
    # Check if empty
    def isEmpty(self):
        return self.length == 0
    
    # Get front or peek item
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.front.data
    
    # Insert an item
    def enqueue(self, element):
        new_node = Node(element)
        if self.rear is None:
            self.front = self.rear = new_node
            self.length += 1
            return
        self.rear.next = new_node
        self.rear = new_node
        self.length += 1
    
    # Remove an item
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        temp = self.front
        self.front = temp.next
        self.length -= 1
        if self.front is None:
            self.rear = None
        return temp.data

    # Print queue
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
q.printQueue()
print("Size: ", q.getSize())
print("Dequeue: ", q.dequeue())
print("Peek: ", q.peek())
print("isEmpty: ", q.isEmpty())
print("Size: ", q.getSize())
