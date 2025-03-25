""" 
Fibonacci with recursion

Recall that Fibonacci numbers is a sequence such that
each number is the sum of the two preceeding ones starting from 0 and 1
So we have 0, 1, 1, 2, 3, 5, 8, 13, 21
"""

# The function
def fibonacci(n):
    if n <= 2:
        return [0, 1][:n]
    sequence = fibonacci(n-1)
    sequence.append(sum(sequence[-2:]))
    return sequence

print(fibonacci(10))