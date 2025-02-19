""" 
Identity matrix
"""
size = 3

def identity(size):
    for row in range(0, size):
        for col in range(0, size):
 
            # Here end is used to stay in same line
            if (row == col):
                print("1 ", end=" ")
            else:
                print("0 ", end=" ")
        print()

print(identity(size))