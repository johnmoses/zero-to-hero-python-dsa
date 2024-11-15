""" 
Insertion Sort algorithm 
It uses one part of the array to hold the sorted values, and the other part of the array to hold values that are not sorted yet
"""

arr = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(arr)
for i in range(1,n):
    insert_index = i
    current_value = arr.pop(i)
    for j in range(i-1, -1, -1):
        if arr[j] > current_value:
            insert_index = j
    arr.insert(insert_index, current_value)

print("Sorted array:", arr)