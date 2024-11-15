""" 
Insertion Sort algorithm 
It uses one part of the array to hold the sorted values, and the other part of the array to hold values that are not sorted yet
"""

def insertion_sort(arr):
    n = len(arr)
    for k in range(1, n):
        cur = arr[k]
        j = k
        while j > 0 and arr[j-1] > cur:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = cur
    return arr

arr = [64, 34, 25, 12, 22, 11, 90, 5]
print(insertion_sort(arr))