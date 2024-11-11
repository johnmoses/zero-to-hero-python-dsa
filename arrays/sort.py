""" 
Sort Array elements
Bubble Sort is an algorithm that sorts an array from the 
lowest value to the highest value
"""
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

array = [64, 34, 25, 12, 22, 11, 90, 5]
print(bubble_sort(array))