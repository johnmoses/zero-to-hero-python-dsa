def openRussianDoll(doll):
    if doll == 1:
        print("All dolls are opened")
    else:
        openRussianDoll(doll-1)

openRussianDoll(4)

def firstMethod():
    secondMethod()
    print("First method")

def secondMethod():
    thirdMethod()
    print("Second method")

def thirdMethod():
    fourthMethod()
    print("Third method")

def fourthMethod():
    print("Fourth method")

firstMethod()

def recursionMethod(n):
    if n<1:
        print("n is less than 1")
    else:
        recursionMethod(n-1)
        print(n)

recursionMethod(5)

# Recursion vs iteration
def powerOfTwo(n):
    if n == 0:
        return 1
    else:
        power = powerOfTwo(n-1)
        return power * 2
print('Power of Two: ', powerOfTwo(3))

def powerOftwoIteration(n):
    i = 0
    power = 1
    while i < n:
        power = power * 2
        i = i + 1
    return power

print('Power of Two iteration: ', powerOftwoIteration(3))

## Factorial
def factorial(n):
    assert n >= 0 and int(n) == n, 'n is positive integer'
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)
print('Factorial: ', factorial(7))

## Fibonacci
def fibonacci(n):
    assert n >=0 and int(n) == n, 'Figonacci number cannot be negative or non integer'
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print('Fibonacci: ', fibonacci(7))
