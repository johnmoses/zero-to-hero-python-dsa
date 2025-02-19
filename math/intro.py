""" 
Basic math
"""
a = 2
b = 3
n = 18

import math 

def add(a, b):
    return a + b

def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = int(n/2)
    for i in range(3, int(math.sqrt(n)) +1, 2):
        while n % i == 0:
            factors.append(i)
            n = int(n/i)
    if n > 2:
        factors.append(n)
    return factors


print(add(a, b))
print(prime_factors(n))