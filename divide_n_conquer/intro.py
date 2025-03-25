"""
Given a list of n integers, find the maximum element in the list. 
Use a divide and conquer approach.

Sample 1 
    input: [1, 4, 3, -5, -4, 8, 6]
    Output: 8
"""

def maxElement(arr):
    """
    Finds the maximum element in the given list using divide and conquer approach.

    Args:
        arr (list): A list of integers.

    Returns:
        int: The maximum element in the list.
    """
    # Base case: If the list has only one element, return that element
    if len(arr) == 1:
        return arr[0]
    
    # Base case: If the list has two elements, return the maximum of the two
    if len(arr) == 2:
        return max(arr[0], arr[1])
    
    # Divide the list into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Recursively find the maximum element in the left and right halves
    left_max = maxElement(left)
    right_max = maxElement(right)
    
    # Return the maximum of the maximum elements from the left and right halves
    return max(left_max, right_max)

# Example usage
arr = [1, 4, 3, -5, -4, 8, 6]
print(maxElement(arr))  # Output: 8

"""
Time Complexity: O(n log n)
Space Complexity: O(log n)
"""
