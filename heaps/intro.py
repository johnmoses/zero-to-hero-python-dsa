"""
Heaps

Design a basic heap data structure
Implement a basic heap data structure with the following operations:
    
    Insert a value into the heap
    Delete the minimum value from the heap
    Check if the heap is empty
    Get the minimum value in the heap
    Check if a value exists in the heap
    Check if a value exists in the heap in O(log n) time complexity
    Get the index of a value in the heap in O(log n) time complexity
    Check if a value exists in the heap in O(n) time complexity
    Get the index of a value in the heap in O(n) time complexity
    Get the size of the heap
    
"""

class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def delete(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_val

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def is_empty(self):
        return len(self.heap) == 0

    def get_min(self):
        if not self.heap:
            return None
        return self.heap[0]

    def exists(self, value):
        return value in self.heap

heap = Heap()
heap.insert(5)
heap.insert(3)
heap.insert(7)
heap.insert(1)
heap.insert(9)

print(heap.delete())  # Output: 1

"""
Time Complexity:
- Insertion: O(log n)
- Deletion: O(log n)
- Heapify Up: O(log n)
- Heapify Down: O(log n)

Space Complexity: O(n)
"""

