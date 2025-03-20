"""
Matrix and Operations
"""
# Defining number of rows and columns in matrix
rows = 3
cols = 3

# Declaring a matrix of size 3 X 3, and 
# initializing it with value zero
rows, cols = (3, 3)
mat1 = [[0]*cols]*rows
print('Matrix 1: ', mat1)

mat2 = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]

# Accessing elements of 2-D array
print("Row 1 column 1:", mat2[0][0])
print("Row 2 column 3:", mat2[1][2])
print("Row 3 column 2:", mat2[2][1])

# Initializing a 2-D list with values
mat3 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# Traversing each row
for row in mat3:
  
    # Traversing each element
    # in the current row
    for x in row:
        print(x, end=" ")
    print()
    