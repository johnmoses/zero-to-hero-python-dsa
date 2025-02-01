"""
Recursion
"""

def recursion(n):
    if n<1:
        print("n is less than 1")
    else:
        recursion(n-1)
        print(n)

recursion(5)