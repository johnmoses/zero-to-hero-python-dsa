"""
Simple Algorithms
Fibonacci numbers
"""

# Using loop
prev2 = 0
prev1 = 1

print(prev2)
print(prev1)
for fibo in range(10):
    next_num = prev1 + prev2
    print(next_num)
    prev2 = prev1
    prev1 = next_num
