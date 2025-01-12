""" 
The equilibrium index of an array is an index such that the sum of
elements at lower indexes is equal to the sum of elements at higher indexes.

Example Input:
arr = [-7, 1, 5, 2, -4, 3, 0]
Output: 3
"""

arr = [-7, 1, 5, 2, -4, 3, 0]

def equilibrium_index(arr: list[int]) -> int:
    total_sum = sum(arr)
    left_sum = 0

    for i, val in enumerate(arr):
        total_sum -= val
        if left_sum == total_sum:
            return i
        left_sum += val
    return -1

print(equilibrium_index(arr))