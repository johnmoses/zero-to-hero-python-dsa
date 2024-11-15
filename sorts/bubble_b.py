""" 
Bubble Sort is an algorithm that sorts an array from the 
lowest value to the highest value
As an improvemennt, a variable 'swapped' is introduced
"""

def bubble_sort_1(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

print(bubble_sort_1(array))
print(bubble_sort_1(array1))