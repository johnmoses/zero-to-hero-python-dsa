"""
Reverse a String
"""
s = ["h","e","l","l","o"]

from typing import List

def reverse_string(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place
    """
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left, right = left + 1, right -1
    print(s)

print(reverse_string(s))