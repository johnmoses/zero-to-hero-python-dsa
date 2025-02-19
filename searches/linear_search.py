""" 
Linear Search
"""
arr = [10, 23, 45, 70, 11, 15]
target = 70

def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1


print(linear_search(arr, target))
