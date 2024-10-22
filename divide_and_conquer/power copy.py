"""
Power
"""

def power(base,exp):
    if exp == 0:
        return 1
    if (exp==1):
        return (base)
    if(exp!=1):
        return (base*power(base,exp-1))

print('Power ', power(5,2))