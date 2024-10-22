"""
Sum of Digits
"""

def sumofDigits(n):
    assert n>=0 and int(n) == n
    if n == 0:
        return 0
    else:
        return int(n%10) + sumofDigits(int(n/10))

print('Sum of digits ', sumofDigits(222))