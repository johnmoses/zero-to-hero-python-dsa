"""
Memoization
"""

def memoize(n):
    print('Computing memoize('+str(n)+')')
    if n <= 1:
        return n
    else:
        return memoize(n - 1) + memoize(n - 2)

print('memoize(6) = ',memoize(6))