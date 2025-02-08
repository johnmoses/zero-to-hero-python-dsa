""" 
Insertion Sort algorithm 
It uses one part of the array to hold the sorted values, and the other part of the array to hold values that are not sorted yet
"""
arr = [64, 34, 25, 12, 22, 11, 90, 5]

def insertion_sort_1(arr):
    n = len(arr)
    for k in range(1, n):
        cur = arr[k]
        j = k
        while j > 0 and arr[j-1] > cur:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = cur
    return arr

print(insertion_sort_1(arr))

def insertion_sort_2(arr):
    n = len(arr)
    for i in range(1,n):
        insert_index = i
        current_value = arr.pop(i)
        for j in range(i-1, -1, -1):
            if arr[j] > current_value:
                insert_index = j
        arr.insert(insert_index, current_value)
    return arr

print(insertion_sort_2(arr))

def insertion_sort_3(arr):
    n = len(arr)
    for i in range(1,n):
        insert_index = i
        current_value = arr[i]
        for j in range(i-1, -1, -1):
            if arr[j] > current_value:
                arr[j+1] = arr[j]
                insert_index = j
            else:
                break
        arr[insert_index] = current_value
    return arr
print(insertion_sort_3(arr))