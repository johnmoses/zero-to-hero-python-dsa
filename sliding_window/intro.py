""" 
Write a sliding window algorithm to 
find the maximum sum of a subarray of size k in an array.

Example:
    Input: arr = [1, 2, 3, 4, 5], k = 3
    Output: 9 (3 + 4 + 5 = 9)
"""
def findMaxSum1(arr, k):
    # Handle edge cases
    if not arr or k <= 0 or k > len(arr):
        return 0
    
    # Calculate sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide window and track maximum sum
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)
        
    return max_sum


def findMaxSum2(arr, k):
    maxSum = 0
    windowSum = 0
    start = 0
    
    for i in range(len(arr)):
        windowSum += arr[i]
        
        if ((i - start + 1) == k):
            maxSum = max(maxSum, windowSum)
            windowSum -= arr[start]
            start += 1
    
    return maxSum

print(findMaxSum1([1, 2, 3, 4, 5], 3))
print(findMaxSum2([1, 2, 3, 4, 5], 3))