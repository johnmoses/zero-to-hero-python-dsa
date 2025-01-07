"""
Merge two Arrays into one
Do not return anything, modify in-place
"""

arr1 = [1,2,3,0,0,0]
arr2 = [2,5,6]
m = 3
n = 3

def merge(arr1, m, arr2, n):
    # Iterate over n
    for i in range(n):
        arr1[i+m] = arr2[i]

    # Sort list in-place
    arr1.sort()
    print(arr1)

merge(arr1, m, arr2, n)