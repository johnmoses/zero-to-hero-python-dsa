""" 
Find Minimum Sum SubArray of Size K

Input: arr = [10, 4, 2, 5, 6, 3, 8, 1]
k = 3
Output: 11
"""

arr = [10, 4, 2, 5, 6, 3, 8, 1]
k = 3

def findMinSum(arr, k):
    currSum = 0
    minSum = float("inf")
    start = 0
    
    for i in range(len(arr)):
        currSum += arr[i]
        
        if (i - start + 1 == k):
            minSum = min(minSum, currSum)
            currSum -= arr[start]
            start += 1
    
    return minSum

print(findMinSum(arr, k))