""" 
Calculate the product sum of a "special" array which can contain integers or nested
arrays. The product sum is obtained by adding all elements and multiplying by their
respective depths.

For example, in the array [x, y], the product sum is (x + y). In the array [x, [y, z]],
the product sum is x + 2 * (y + z). In the array [x, [y, [z]]],
the product sum is x + 2 * (y + 3z).

Example Input:
[5, 2, [-7, 1], 3, [6, [-13, 8], 4]]
Output: 12
"""

arr = [5, 2, [-7, 1], 3, [6, [-13, 8], 4]]

def product_sum(arr: list[int | list], depth: int) -> int:
    total_sum = 0
    for e in arr:
        total_sum += product_sum(e, depth + 1) if isinstance(e, list) else e
        return total_sum * depth

print(product_sum(arr,1))
