"""
Write a basic divide and conquer function
that divides a list into two halves
and returns the two halves as separate lists.
Example usage:
    >>> divide_list([1, 2, 3, 4, 5, 6])
    ([1, 2, 3], [4, 5, 6])
"""

def divide_list(list):
    """
    Divides a given list into two halves and returns them as separate lists.

    Args:
        list (list): The list to be divided.

    Returns:
        tuple: A tuple containing two lists, representing the two halves of the original list.
    """
    # Calculate the midpoint index of the list
    midpoint = len(list) // 2
    
    # Create two new lists by slicing the original list
    # The first list contains elements from the start to the midpoint (exclusive)
    # The second list contains elements from the midpoint to the end
    return list[:midpoint], list[midpoint:]

print(divide_list([1, 2, 3, 4, 5, 6]))
