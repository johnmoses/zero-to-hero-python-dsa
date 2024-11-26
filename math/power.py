""" 
Power
Performs exponentiation, similar to built-in pow() or ** feature
"""

def power(a: int, n: int, mod: int = None):
    ans = 1
    while n:
        if n & 1:
            ans = ans * a
        a = a * a
        if mod:
            ans %= mod
            a %= mod
        n >>= 1
    return ans

a = 2
n = 2
print(power(a,n))