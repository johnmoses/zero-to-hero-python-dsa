"""
Power
"""

def power(base, exponent):
    if exponent == 0:
        return 1
    if (exponent==1):
        return (base)
    if(exponent!=1):
        return (base*power(base,exponent-1))
    
def power_1(base, exponent):
    if exponent == 0:
        return 1
    return base * power_1(base, exponent-1)

def power_slow(x, n):
    if n == 0:
        return 1
    else:
        return x * power_1(x, n-1)
    
def power_fast(x, n):
    if n == 0:
        return 1
    else:
        partial = power_1(x, n // 2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result

print(power(5,2))
print(power_slow(5,2))
print(power_fast(5,2))
