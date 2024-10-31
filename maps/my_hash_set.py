"""
Hash Set example
"""

class MyHashSet:

    def __init__(self):
        # data structure
        self.table = [0] * 1000000

    def add(self, key: int) -> None:
        self.table[key] = 1

    def remove(self, key: int) -> None:
        self.table[key] = 0

    def contains(self, key: int) -> bool:
        # Return true if it has the element
        return self.table[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
obj = MyHashSet()
print(obj)
obj.add(1)
print(obj.contains(2))
# Output [null, null, null, true, false, null, true, null, false]