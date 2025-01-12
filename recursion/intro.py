"""
Recursion
"""

def recursionMethod(n):
    if n<1:
        print("n is less than 1")
    else:
        recursionMethod(n-1)
        print(n)

recursionMethod(5)