"""
Simple Recursion
"""

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

def factorial1(n):
    assert n >= 0 and int(n) == n, 'n is positive integer'
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
print(factorial1(5))