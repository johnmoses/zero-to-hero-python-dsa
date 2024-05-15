"""
Array Stack
"""

class ArrayStack:
    def __init__(self):
        self._data = []
    
    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0
    
    def top(self):
        if self.is_empty():
            # raise Empty('Stack is empty')
            raise Exception('Stack is empty')
        return self._data[-1]

    def push(self, e):
        self._data.append(e)

    def pop(self):
        if self.is_empty():
            # raise Empty("Stack is empty")
            raise Exception('Stack is empty')
        return self._data.pop()


if __name__ == "__main__":
    s = ArrayStack()
    s.push(5)
    s.push(3)

    print(len(s))
    print(s.pop())
    print(s.is_empty())
    print(s.pop())
    print(s.is_empty())
    s.push(7)
    s.push(9)
    print(S.top())
    s.push(4)
    print(len(s))
    print(s.pop())
    s.push(6)
    s.push(8)
    print(s.pop())
    