"""
Linear search
The Linear Search algorithm searches through an array and returns the index of the value it searches for.
T(n): O(n)
"""

arr1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
arr2 = ['A','B','D','G','C','F','E']
target1 = 9
target2 = 'B'

def linear_search(arr, target):
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return i
    return -1

print(linear_search(arr1, target1))
print(linear_search(arr2, target2))

def linear_search_2(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

print(linear_search_2(arr1, target1))
print(linear_search_2(arr2, target2))