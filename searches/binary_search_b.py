""" 
Binary Search of an array
"""

def binary_search(arr, target):
    # Initialize variables
    left = 0
    right = len(arr) -1

    # Iterate over array
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid

arr1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
arr2 = ['A','B','D','G','C','F','E']
target1 = 9
target2 = 'B'

print(binary_search(arr1, target1))
print(binary_search(arr2, target2))