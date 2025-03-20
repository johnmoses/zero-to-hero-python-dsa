""" 
Search algorithm

Write a search algorithm 

1. Linear search
2. Binary search


Example:
    
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 9

"""
def linear_search(arr, target):
    """Simple linear search through array"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    """Binary search for sorted array"""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid

print(linear_search([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 9))
print(binary_search([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 9))