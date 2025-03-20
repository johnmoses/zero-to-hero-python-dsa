"""
Write a Function that can reverse a string using stack data structure
"""
def reverse_string_1(string):
    stack = []
    for char in string:
        stack.append(char)
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()
    return reversed_string

print(reverse_string_1("MAPS"))

def reverse_string_2(s):
    stack = []

    for ch in s:
        stack.append(ch)
    revstr = ''
    while len(stack)!=0:
        revstr += stack.pop()
    return revstr

print(reverse_string_2("MAPS"))