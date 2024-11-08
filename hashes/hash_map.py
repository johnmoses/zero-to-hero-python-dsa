"""
Hash Map
"""

class HashMap:
    def __init__(self):
        self.hm = {}

    def put(self, key: int, val: int) -> None:
        self.hm[key] = val

    def get(self, key: int) -> int:
        return self.hm[key] if key in self.hm else -1

    def remove(self, key: int) -> None:
        if key in self.hm:
            del self.hm[key]

    

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

hm = HashMap()
hm.put(1,1)
hm.put(2,2)
param_1 = hm.get(1)
hm.remove(1)
print(param_1)