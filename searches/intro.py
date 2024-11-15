"""
Linear search
The Linear Search algorithm searches through an array and returns the index of the value it searches for.
"""

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
arr2 = ['A','B','D','G','C','F','E']
target1 = 9
target2 = 'B'

print(linear_search(arr1, target1))
print(linear_search(arr2, target2))