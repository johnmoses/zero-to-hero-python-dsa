""" 
Quick Sort
"""

from random import randrange

def quick_sort(data: list) -> list:
    """ 
    data: a mutable collection of comparable items
    return: return value
    """
    # Check if list has at least 2 items
    if len(data) < 2:
        return data
    # Select pivot index at random and remove it
    pivot_index = randrange(len(data))
    pivot = data.pop(pivot_index)

    # Partition remaining items into two groups
    