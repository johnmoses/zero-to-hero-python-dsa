""" 
Multimaps

Write a basic implementation of a multimap data structure with basic behaviours
"""
class MultiMap:
    def __init__(self):
        self.data = []

    def set(self, key, value):
        for item in self.data:
            if item[0] == key:
                item[1].append(value)
                return
        self.data.append([key, [value]])

    def get(self, key):
        for item in self.data:
            if item[0] == key:
                return item[1]
        return None

    def has(self, key):
        for item in self.data:
            if item[0] == key:
                return True
        return False

    def delete(self, key):
        for i, item in enumerate(self.data):
            if item[0] == key:
                del self.data[i]
                return True
        return False

    def __str__(self):
        return str(self.data)

# Example usage
m = MultiMap()
m.set("a", 1)
m.set("a", 2)
m.set("b", 3)
print(m)
print(m.get("a"))  # Output: [1, 2]
print(m.has("b"))  # Output: True
m.delete("a")
print(m.has("a"))  # Output: False
print(m)