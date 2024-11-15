"""
Simple Bubble Sort Algorithm
Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order
"""

arr = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(arr)
for i in range(n-1):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print("Sorted array:", arr)