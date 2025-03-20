"""
Memoization

Write a basic memoization algorithm that computes the nth Fibonacci number.
"""

def memoize(n, cache=None):
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    else:
        cache[n] = memoize(n - 1, cache) + memoize(n - 2, cache)
        return cache[n]

print('memoize(6) = ', memoize(6))

"""
memoize(6) =  8
"""

# def memoize(n):
#     print('Computing memoize('+str(n)+')')
#     if n <= 1:
#         return n
#     else:
#         return memoize(n - 1) + memoize(n - 2)

# print('memoize(6) = ',memoize(6))