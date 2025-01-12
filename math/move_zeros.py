"""
Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements.

The time complexity of the below algorithm is O(n).
"""

array = [False, 1, 0, 1, 2, 0, 1, 3, "a"]

def move_zeros(array):
    # Define and initialize result res and zeroes
    res = []
    zeros = 0
    
    # Iterate over the array
    # Check for zeros and non-bolean values
    for i in array:
        if i == 0 and type(i) != bool:
            zeros += 1
        else:
            res.append(i)
    res.extend([0] * zeros)
    return res

print(move_zeros(array))