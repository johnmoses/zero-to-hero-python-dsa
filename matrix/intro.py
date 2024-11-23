"""
Matrix and Operations
"""
# Defining number of rows and columns in matrix
rows = 3
cols = 3

# Declaring a matrix of size 3 X 3, and 
# initializing it with value zero
rows, cols = (3, 3)
arr = [[0]*cols]*rows
print(arr)

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];

# Accessing elements of 2-D array
print("First element of first row:", arr[0][0])
print("Third element of second row:", arr[1][2])
print("Second element of third row:", arr[2][1])

# Initializing a 2-D list with values
arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# Traversing each row
for row in arr:
  
    # Traversing each element
    # in the current row
    for x in row:
        print(x, end=" ")
    print()