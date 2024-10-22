"""
Simple Data structure
"""

def product_sum(arr: list[int | list], depth: int) -> int:
    """ 
    Using recursive approach, get sum of each element multiplied by
    their respective depths.
    It it is a list, add one to the depth
    """
    total_sum = 0
    for item in arr:
        total_sum += product_sum(item, depth + 1) if isinstance(item, list) else item
    return total_sum * depth

arr = [1, 2, 3]
depth = 1
print(product_sum(arr, depth))