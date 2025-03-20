"""
Write dynamic programing algorithm for nth fibonacci number

"""
def nthFibo1(n):
    if n==0: 
        return 0
    if n==1: 
        return 1
    return nthFibo1(n-1) + nthFibo1(n-2)

def nthFibo2(n):
    if n==0: 
        return 0
    if n==1: 
        return 1

    F = [None] * (n + 1)
    F[0] = 0
    F[1] = 1

    for i in range(2, n + 1):
        F[i] = F[i - 1] + F[i - 2]

    return F[n]

print(nthFibo1(10))
print(nthFibo2(10))
