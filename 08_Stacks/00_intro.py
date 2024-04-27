"""
Stacks
"""
s = []
s.append('https://www.cnn.com')
s.append('https://www.cnn.com/world')
s.append('https://www.cnn.com/africa')

# pop
s.pop()
print(s)

print(s[-1])

# create stack from library
from collections import deque

stack = deque()

print(dir(stack))
