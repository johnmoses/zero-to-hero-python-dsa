""" 
Fibonacci with recursion
"""

print(0)
print(1)
count = 2

def fibonacci(prev1, prev2):
    global count
    if count <= 10:
        next_num = prev1 + prev2
        print(next_num)
        prev2 = prev1
        prev1 = next_num
        count += 1
        fibonacci(prev1, prev2)
    else:
        return

fibonacci(1,0)