"""
Simple Sort Algorithm

Write a basic sort algorithm that takes a list of numbers and returns a sorted list.

This code defines a function `sort` that takes a list of numbers as input and returns a sorted list.
The `sort` function uses the built-in `sorted` function to sort the input list.

Sample Input:
    nums = [1, 5, 2, 3, 4]

Sample Output:
    [1, 2, 3, 4, 5]
"""

def sort(nums):
    """
    Sort a list of numbers in ascending order.

    Args:
        nums (list): A list of numbers to be sorted.

    Returns:
        list: A new list containing the sorted numbers.
    """
    return sorted(nums)

print(sort([1, 5, 2, 3, 4]))
