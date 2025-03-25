"""
Array
Write a basic array data structure

Example usage:
    array = [6, 13, 9, 3, 11, 19]
"""

class Array:
    def __init__(self, initial_elements):
        self.data = initial_elements

    def search(self, target):
        for element in self.data:
            if element == target:
                return True
        return False

    def insert(self, element):
        self.data.append(element)

    def delete(self, element):
        for i in range(len(self.data)):
            if self.data[i] == element:
                del self.data[i]
                return
        print(f"Element {element} not found")

    def traverse(self):
        for element in self.data:
            print(element)

# Example usage:
array = Array([6, 13, 9, 3, 11, 19])
print(array.search(13))  # Output: True
array.insert(8)
array.traverse()  # Output: 6, 13, 9, 3, 11, 19, 8
array.delete(3)
array.traverse()  # Output: 6, 13, 9, 11, 19, 8
