"""
Reverse String
"""

from deque_stack import DequeStack

# Function that can reverse a string using stack data structure
def reverse_string(s):
    stack = DequeStack()

    for ch in s:
        stack.push(ch)
    revstr = ''
    while stack.size()!=0:
        revstr += stack.pop()
    return revstr

if __name__ == '__main__':
    s = "MAPS"
    print(reverse_string(s))