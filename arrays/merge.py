"""
Merge two Arrays into one
Do not return anything, modify in-place

arr1 = [1,2,3,0,0,0]
arr2 = [2,5,6]
m = 3
n = 3
"""

def merge1(arr1, arr2, m, n):
    i = m - 1
    j = n - 1
    k = m + n - 1

    while i >= 0 and j >= 0:
        if arr1[i] > arr2[j]:
            arr1[k] = arr1[i]
            i -= 1
        else:
            arr1[k] = arr2[j]
            j -= 1
        k -= 1

    while j >= 0:
        arr1[k] = arr2[j]
        j -= 1
        k -= 1

def merge2(arr1, m, arr2, n):
    # Iterate over n
    for i in range(n):
        arr1[i+m] = arr2[i]

    # Sort list in-place
    arr1.sort()
    print(arr1)

print(merge1([1,2,3,0,0,0], [2,5,6], 3, 3))
# merge2([1,2,3,0,0,0], [2,5,6], 3, 3)