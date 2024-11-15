"""
Selection Sort
"""

def selection_sort(arr):
    # Get size of array
    n = len(arr)

    # Iterate through array
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]

tests = [
    [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
    [],
    [1,5,9,8],
    [234,3,1,56,34,12,9,12,1300],
    [78, 12, 15, 8, 61, 53, 23, 27],
    [5]
]
for elements in tests:
    selection_sort(elements)
    print(elements)